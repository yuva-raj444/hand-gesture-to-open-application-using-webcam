import cv2
import mediapipe as mp
import subprocess
import time

# Initialize Mediapipe hands and drawing utilities
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Define the application mapping to hand gestures (Custom applications)
applications = {
    1: 'notepad.exe',   # Thumb up -> Notepad (Windows)
    2: 'calc.exe',      # Peace sign -> Calculator (Windows)
    3: 'chrome',        # Open palm -> Chrome browser
    4: 'explorer.exe',  # Fist -> File Explorer (Windows)
    5: 'mspaint.exe',   # Thumb and Pinky -> Paint (Windows)
    6: 'vlc',           # VLC Media Player
    7: 'spotify',       # Spotify
    8: 'code',          # Visual Studio Code
    9: 'firefox',       # Firefox browser
    10: 'gedit',        # Gedit (Linux Text Editor)
}

# Helper function to launch an application based on gesture ID
def launch_application(gesture_id):
    if gesture_id in applications:
        app = applications[gesture_id]
        try:
            subprocess.Popen([app])
            print(f"Launched: {app}")
        except Exception as e:
            print(f"Failed to launch {app}: {e}")

# Function to recognize a gesture based on landmarks
def recognize_gesture(landmarks):
    # Finger positions based on hand landmarks
    thumb_is_open = landmarks[4].y < landmarks[3].y
    index_is_open = landmarks[8].y < landmarks[6].y
    middle_is_open = landmarks[12].y < landmarks[10].y
    ring_is_open = landmarks[16].y < landmarks[14].y
    pinky_is_open = landmarks[20].y < landmarks[18].y

    # Define 10 unique gestures
    if thumb_is_open and not index_is_open and not middle_is_open and not ring_is_open and not pinky_is_open:
        return 1  # Gesture 1: Thumb up -> Notepad
    elif not thumb_is_open and index_is_open and middle_is_open and not ring_is_open and not pinky_is_open:
        return 2  # Gesture 2: Peace sign -> Calculator
    elif thumb_is_open and index_is_open and middle_is_open and ring_is_open and pinky_is_open:
        return 3  # Gesture 3: Open palm -> Chrome
    elif not thumb_is_open and not index_is_open and not middle_is_open and not ring_is_open and not pinky_is_open:
        return 4  # Gesture 4: Fist -> File Explorer
    elif thumb_is_open and not index_is_open and not middle_is_open and not ring_is_open and pinky_is_open:
        return 5  # Gesture 5: Thumb and Pinky -> Paint
    elif not thumb_is_open and index_is_open and not middle_is_open and not ring_is_open and pinky_is_open:
        return 6  # Gesture 6: Spock sign -> VLC Player
    elif not thumb_is_open and index_is_open and middle_is_open and ring_is_open and pinky_is_open:
        return 7  # Gesture 7: Four fingers -> Spotify
    elif thumb_is_open and index_is_open and middle_is_open and not ring_is_open and not pinky_is_open:
        return 8  # Gesture 8: Thumb, Index, Middle -> Visual Studio Code
    elif not thumb_is_open and index_is_open and not middle_is_open and ring_is_open and pinky_is_open:
        return 9  # Gesture 9: Index, Ring, Pinky -> Firefox
    elif thumb_is_open and not index_is_open and middle_is_open and not ring_is_open and pinky_is_open:
        return 10  # Gesture 10: Custom -> Gedit

    return None  # No valid gesture detected

# Initialize webcam
cap = cv2.VideoCapture(0)

# Initialize Mediapipe Hands solution
with mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7) as hands:

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Flip the frame horizontally for a selfie-view display
        frame = cv2.flip(frame, 1)
        
        # Convert the BGR image to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Process the frame to detect hand landmarks
        result = hands.process(rgb_frame)
        
        # Draw the hand annotations on the frame
        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Get list of landmarks for gesture recognition
                landmarks = hand_landmarks.landmark

                # Recognize the gesture and launch the corresponding application
                gesture_id = recognize_gesture(landmarks)
                if gesture_id:
                    launch_application(gesture_id)
                    time.sleep(1)  # Adding a delay to avoid multiple launches
                
        # Display the frame with annotations
        cv2.imshow('Hand Gesture App Launcher', frame)
        
        # Break loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release resources
cap.release()
cv2.destroyAllWindows()