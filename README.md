# Hand Gesture to Open Application Using Webcam

This project utilizes hand gesture recognition to launch applications on your computer. It uses a **webcam** to detect hand gestures in real-time and opens predefined applications based on the recognized gestures.

## Features
- Detects various hand gestures using a **webcam**.
- Launches specific applications like **Notepad**, **Calculator**, **MS Paint**, **VLC**, **Spotify**, etc., based on the gestures.
- Closes the most recent visible window when an "Open Palm" gesture is detected.

## Requirements

### Python Packages
Make sure you have the following libraries installed:
- `opencv-python`: For webcam access and image processing.
- `mediapipe`: For hand gesture recognition.
- `numpy`: For mathematical computations.
- `pywin32`: For interacting with Windows applications and closing windows.
- `subprocess`: To launch applications.

You can install them using pip:

```bash
pip install opencv-python mediapipe numpy pywin32
```
Additional Tools:
Windows operating system (for interaction with Windows applications via pywin32).

How to Run
1. Clone the repository:
Clone the project to your local machine using Git:

```bash
git clone https://github.com/yuva-raj444/hand-gesture-to-open-application-using-webcam.git
```
2. Navigate to the project folder:
```bash
cd hand-gesture-to-open-application-using-webcam
```
3. Run the Python script:
Start the application by running the hand_gesture_app.py file.
```bash
python hand_gesture_app.py

```
4. Usage:
Point your hand in front of the webcam and perform the following gestures to open the corresponding applications:

👍 Thumb Up: Opens Notepad.

✌ Peace Sign: Opens Calculator.

✊ Fist: Opens Command Prompt.

🤙 Shaka: Opens MS Paint.

👆 Index Finger Up: Opens File Explorer.

🤞 Crossed Fingers: Opens VLC Media Player.

🖖 Spock Hand: Opens Spotify.

👌 OK Sign: Opens Snipping Tool.

🤜 Punch Gesture: Opens Task Manager.

🖐️ Open Palm: Closes the most recent visible window (excluding OpenCV and Visual Studio Code).

5. Exit the application:
To exit the application, press q on the keyboard.

# Code Structure

The project consists of the following main parts:

## Gesture Recognition:

The hand gesture recognition is done using the mediapipe library, which detects the landmarks of the hand and compares the positions of the fingers to recognize predefined gestures.

## Application Launching:

The application corresponding to the recognized gesture is launched using Python's subprocess module.

## Window Management:

The pywin32 library is used to close the most recent visible window excluding OpenCV and Visual Studio Code.

## Troubleshooting
Camera not detected: Ensure your webcam is working and accessible by other applications.

Applications not launching: Check the mappings in the code to ensure the correct executable names are used (e.g., notepad.exe for Notepad).

Gesture not recognized: Ensure the camera is properly aligned with your hand and the lighting is sufficient.
