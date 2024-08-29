# Virtual Mouse Project

## Project Overview
The Virtual Mouse project aims to develop a system that allows users to control their computer's mouse pointer using hand gestures captured through a camera. This project leverages computer vision techniques to recognize hand gestures and translate them into mouse movements and clicks, providing a touchless and intuitive way to interact with a computer.

## Features
- **Hand Gesture Recognition**: The system detects and interprets various hand gestures to perform actions like moving the cursor, left-click, right-click, and more.
- **Real-time Tracking**: Utilizes computer vision algorithms for real-time hand tracking and gesture detection.
- **Modular Design**: Separate modules for tracking and gesture recognition for easy maintenance and scalability.
- **Python-based Implementation**: Developed using Python, making it easily extensible and compatible with various platforms.

## Technologies Used
- **Programming Language**: Python
- **Computer Vision Libraries**: OpenCV, MediaPipe
- **Development Environment**: Jupyter Notebook, Visual Studio Code
- **Dependencies**: 
  - OpenCV
  - MediaPipe

## System Architecture
The system architecture is designed to efficiently capture, process, and interpret hand gestures:
- **Input Layer**: Captures video feed from the camera.
- **Processing Layer**: Applies computer vision techniques to detect hand landmarks and interpret gestures.
- **Output Layer**: Translates gestures into corresponding mouse actions.

## Key Components
- **app.py**: The main application script that runs the virtual mouse system.
- **tracking_module.py**: Contains the code for hand tracking and gesture recognition.
- **README.md**: Documentation file providing an overview of the project.
