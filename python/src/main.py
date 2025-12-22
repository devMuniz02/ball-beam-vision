import cv2
import time
import serial
from controller import PIDController

def main():
    # Initialize the camera
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Camera not accessible.")
        return

    # Initialize the PID controller
    pid = PIDController(kp=1.0, ki=0.1, kd=0.05)
    
    # Initialize serial communication with Arduino
    arduino = serial.Serial('/dev/ttyUSB0', 9600)
    time.sleep(2)  # Wait for the connection to establish

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Frame not captured.")
            break

        # Process the frame to detect the ball
        ball_position = detect_ball(frame)  # This function should be defined in vision.py

        if ball_position is not None:
            # Calculate the control signal using PID
            control_signal = pid.update(ball_position)
            arduino.write(control_signal.encode())  # Send control signal to Arduino

        # Display the frame
        cv2.imshow('Ball and Beam', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    arduino.close()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()