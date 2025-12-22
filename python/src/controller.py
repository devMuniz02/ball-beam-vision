class PIDController:
    def __init__(self, Kp, Ki, Kd, setpoint):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.setpoint = setpoint
        self.previous_error = 0
        self.integral = 0

    def update(self, measured_value, dt):
        error = self.setpoint - measured_value
        self.integral += error * dt
        derivative = (error - self.previous_error) / dt
        output = self.Kp * error + self.Ki * self.integral + self.Kd * derivative
        self.previous_error = error
        return output

def main():
    import serial
    import time

    # PID parameters
    Kp = 1.0
    Ki = 0.1
    Kd = 0.05
    setpoint = 0.0  # Desired position of the ball

    pid = PIDController(Kp, Ki, Kd, setpoint)

    # Setup serial communication with Arduino
    arduino = serial.Serial('/dev/ttyUSB0', 9600)
    time.sleep(2)  # Wait for the connection to establish

    try:
        while True:
            # Read the current position of the ball from Arduino
            arduino.write(b'GET_POSITION\n')
            position = float(arduino.readline().strip())

            # Update the PID controller
            dt = 0.1  # Time step
            control_signal = pid.update(position, dt)

            # Send control signal to Arduino
            arduino.write(f'SET_MOTOR {control_signal}\n'.encode())

            time.sleep(dt)

    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        arduino.close()

if __name__ == "__main__":
    main()