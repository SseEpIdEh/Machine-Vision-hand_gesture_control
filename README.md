# Machine-Vision-hand_gesture_control- and count the fingers


Hand Gesture Control using OpenCV and cvzone.
This repository contains a Python script that enables hand gesture control using the OpenCV and cvzone libraries. With this script, you can control your mouse cursor and perform clicks using hand gestures.

**Installation**,
To use this script, you need to have the following dependencies installed:

Python 3,
OpenCV,
cvzone,
pyautogui,
Usage,
To run the script, follow these steps:

Clone the repository to your local machine.
Connect a webcam to your computer.
Open a terminal and navigate to the repository directory.


****The script will access your webcam and display the video feed.
Perform hand gestures in front of the webcam to control the mouse cursor:
**If you raise your index finger and lower your middle finger, the cursor will move to the right.**
**If you raise your middle finger and lower your index finger, the cursor will move to the left.**
**If you raise your little finger (pinky), a mouse click will be performed.**

**Customization and Extension
This script provides a basic implementation of hand gesture control. 
You can further customize and extend the functionality based on your requirements. Feel free to explore the code and make modifications as needed.**

Contributions
Contributions to this repository are welcome. If you have any improvements, bug fixes, or additional features to add, please feel free to create a pull request.****
*******************************************************************************************************************
**FINGER COUNTER

**This project utilizes computer vision techniques to count the number of fingers shown in front of a webcam. By tracking hand landmarks, the program detects the open or closed state of each finger and provides a real-time count.**

***Features**
1.Uses the webcam to capture video frames
2.Detects hand landmarks using the Mediapipe library
3.Determines the open or closed state of each finger
4.Calculates and displays the number of fingers
5.Provides a visual representation of the finger count on the video frame
**Prerequisites**
Python 3.x
OpenCV library
Mediapipe library
Webcam connected to the computer
**Usage**
-Install the required libraries by running pip install opencv-python mediapipe.
-Connect a webcam to your computer.
-Run the script main.py.
-Position your hand in front of the webcam.
-Observe the finger count displayed on the video frame.
***Acknowledgments**
This project is based on the work of the HandModule library for hand tracking.


