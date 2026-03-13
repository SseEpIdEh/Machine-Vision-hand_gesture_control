# Real-Time Hand Gesture Recognition for Human–Computer Interaction

This project implements a real-time **hand gesture recognition system** using computer vision techniques. The system uses a webcam to detect and track hand landmarks and translates specific gestures into interactive computer commands such as cursor movement and mouse clicks.

The project is implemented in **Python** using the **OpenCV**, **MediaPipe**, and **cvzone** libraries, enabling efficient real-time video processing and gesture interpretation.

## Key Features

* Real-time hand detection and tracking using **MediaPipe hand landmark estimation**
* Gesture-based control of the computer cursor
* Gesture-triggered mouse click actions
* Real-time visual feedback through the webcam video stream
* Modular implementation for easy extension to other gesture-based control applications

## System Workflow

1. Capture video frames from a webcam.
2. Detect and track hand landmarks using MediaPipe.
3. Identify the state of each finger (open or closed).
4. Interpret specific gesture patterns.
5. Convert gestures into control commands for the operating system.

## Gesture Controls

* **Index finger raised** → Move cursor to the right
* **Middle finger raised** → Move cursor to the left
* **Pinky finger raised** → Perform a mouse click

These gestures demonstrate how computer vision can be used to enable **touchless human–computer interaction**.

---

# Finger Counting using Computer Vision

This module demonstrates a **real-time finger counting system** using computer vision techniques. By detecting hand landmarks and analyzing finger positions, the system determines how many fingers are raised and displays the result on the video feed.

## Features

* Capture real-time video from a webcam
* Detect hand landmarks using **MediaPipe**
* Identify the open or closed state of each finger
* Compute the number of raised fingers
* Display the finger count directly on the video frame

## Requirements

* Python 3.x
* OpenCV
* MediaPipe
* Webcam

Install required libraries:

```bash
pip install opencv-python mediapipe
```

## How to Run

1. Clone this repository.
2. Connect a webcam to your computer.
3. Install the required dependencies.
4. Run the main script:

```bash
python main.py
```

5. Position your hand in front of the camera to observe real-time finger detection and counting.

---

## Applications

This project demonstrates the potential of **vision-based interaction systems**, which can be extended to applications such as:

* Human–computer interaction
* Gesture-based device control
* Robotics interfaces
* Touchless control systems
* Assistive technologies

---

💡 **Suggestion (important for internship applications):**
At the top of your GitHub README, add one sentence like this:

> This project demonstrates practical experience with **real-time computer vision, human–machine interaction, and sensor-based input processing**, which are relevant to robotics perception and intelligent interface systems.


---



