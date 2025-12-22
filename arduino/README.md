# Ball-and-Beam Controller Arduino Setup

This README provides instructions specific to the Arduino setup for the Ball-and-Beam controller project.

## Overview

The Ball-and-Beam controller is a system that uses a ball on a beam, controlled by a motor, to balance the ball at a desired position. The system utilizes a PID controller to achieve stability and responsiveness.

## Requirements

- Arduino board (e.g., Arduino Uno)
- Arduino IDE installed on your computer
- USB cable to connect the Arduino to your computer

## Uploading the Sketch

1. Open the Arduino IDE.
2. Connect your Arduino board to your computer using the USB cable.
3. Open the `BallAndBeam.ino` file located in the `arduino` directory.
4. Select the correct board and port from the Tools menu.
5. Click on the upload button (right arrow icon) to upload the sketch to your Arduino.

## Configuration

Ensure that the following configurations are set in the Arduino sketch:

- Pin assignments for the motor and sensors are correctly defined.
- Adjust the PID parameters (Kp, Ki, Kd) in the sketch for optimal performance based on your system's characteristics.

## Serial Communication

The Arduino communicates with the Python application via serial. Make sure to:

- Set the correct baud rate in both the Arduino sketch and the Python code (typically 9600).
- Use the appropriate serial port in the Python application to establish communication.

## Troubleshooting

- If the Arduino does not respond, check the USB connection and ensure the correct port is selected in the Arduino IDE.
- Monitor the serial output for any error messages or debugging information.

## Additional Resources

Refer to the `docs` directory for detailed wiring diagrams, control design documentation, and tuning guidelines for the PID controller.