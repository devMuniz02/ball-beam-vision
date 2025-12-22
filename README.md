# Ball-and-Beam Controller Project

## Overview
The Ball-and-Beam controller project is an interactive system that utilizes a PID controller to balance a ball on a beam. The system consists of an Arduino that controls the beam's angle based on the position of the ball detected by a camera. The Python application interfaces with the Arduino to manage the control logic and provide a user-friendly interface for monitoring and adjustments.

## System Components
- **Arduino**: The microcontroller that reads sensor data, controls the motors, and implements the PID control algorithm.
- **Camera**: Captures video of the ball and processes the frames to detect its position.
- **Python Application**: Manages communication with the Arduino, processes camera input, and implements the control logic.

## Quickstart Instructions
1. **Hardware Setup**: Follow the wiring instructions in the `docs/wiring.md` file to connect the Arduino, motors, and camera.
2. **Arduino Code**: Upload the Arduino sketch located in `arduino/BallAndBeam.ino` to your Arduino board.
3. **Python Environment**: Set up a Python environment and install the required dependencies listed in `python/requirements.txt`.
4. **Run the Application**: Execute the main Python script located in `python/src/main.py` to start the system.

## Serial Protocol
The communication between the Arduino and the Python application is done via a serial interface. The following commands are used:
- **GET_POSITION**: Request the current position of the ball from the Arduino.
- **SET_MOTOR**: Send motor control commands to the Arduino to adjust the beam's angle.

Refer to the `python/src/controller.py` file for detailed implementation of the communication protocol.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.