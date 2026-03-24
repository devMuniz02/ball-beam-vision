[![ArXiv](https://img.shields.io/badge/ArXiv-2512.16841-B31B1B?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2512.16841)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-devmuniz-0A66C2?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/devmuniz)
[![GitHub Profile](https://img.shields.io/badge/GitHub-devMuniz02-181717?logo=github&logoColor=white)](https://github.com/devMuniz02)
[![Portfolio](https://img.shields.io/badge/Portfolio-devmuniz02.github.io-0F172A?logo=googlechrome&logoColor=white)](https://devmuniz02.github.io/)
[![Hugging Face](https://img.shields.io/badge/Hugging%20Face-manu02-FFD21E?logoColor=black)](https://huggingface.co/manu02)

# Ball-and-Beam Controller Project

Refer to the `python/src/controller.py` file for detailed implementation of the communication protocol.

## Overview

Arduino and Python system for real-time ball-and-beam stabilization using computer vision feedback, PID control, and MPU-6050 tilt sensing.

## Repository Structure

| Path | Description |
| --- | --- |
| `arduino/` | Top-level project directory containing repository-specific resources. |
| `assets/` | Images, figures, or other supporting media used by the project. |
| `python/` | Top-level project directory containing repository-specific resources. |
| `venv-ball/` | Top-level project directory containing repository-specific resources. |
| `.gitignore` | Top-level file included in the repository. |
| `camera.py` | Top-level file included in the repository. |
| `LICENSE` | Repository license information. |
| `README.md` | Primary project documentation. |

## Getting Started

1. Clone the repository.

   ```bash
   git clone https://github.com/devMuniz02/ball-beam-vision.git
   cd ball-beam-vision
   ```

2. Prepare the local environment.

Review the repository files below to identify the appropriate local setup steps for this project.

3. Run or inspect the project entry point.

Use the project-specific scripts or notebooks in the repository root to run the workflow.

## Quickstart Instructions

1. **Hardware Setup**: Follow the wiring instructions in the `docs/wiring.md` file to connect the Arduino, motors, and camera.
2. **Arduino Code**: Upload the Arduino sketch located in `arduino/BallAndBeam.ino` to your Arduino board.
3. **Python Environment**: Set up a Python environment and install the required dependencies listed in `python/requirements.txt`.
4. **Run the Application**: Execute the main Python script located in `python/src/main.py` to start the system.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Overview

The Ball-and-Beam controller project is an interactive system that utilizes a PID controller to balance a ball on a beam. The system consists of an Arduino that controls the beam's angle based on the position of the ball detected by a camera. The Python application interfaces with the Arduino to manage the control logic and provide a user-friendly interface for monitoring and adjustments.

## System Components

- **Arduino**: The microcontroller that reads sensor data, controls the motors, and implements the PID control algorithm.
- **Camera**: Captures video of the ball and processes the frames to detect its position.
- **Python Application**: Manages communication with the Arduino, processes camera input, and implements the control logic.

## Serial Protocol

The communication between the Arduino and the Python application is done via a serial interface. The following commands are used:
- **GET_POSITION**: Request the current position of the ball from the Arduino.
- **SET_MOTOR**: Send motor control commands to the Arduino to adjust the beam's angle.

Refer to the `python/src/controller.py` file for detailed implementation of the communication protocol.
