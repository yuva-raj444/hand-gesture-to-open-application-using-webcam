import cv2
import mediapipe as mp
import time

from gesture_recognition import recognize_gesture
from app_launcher import launch_application, applications
from window_manager import close_recent_window, get_opencv_window_handle

# Initialize Mediapipe hands and drawing utilities
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Initialize webcam
cap = cv2.VideoCapture(0)
cv2.namedWindow("Hand Gesture App Launcher")
time.sleep(1)
opencv_hwnd = get_opencv_window_handle()

cooldown_seconds = 3
last_action_time = 0
last_gesture = None

with mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.8, min_tracking_confidence=0.8) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb_frame)
        current_time = time.time()

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                landmarks = hand_landmarks.landmark
                gesture_id = recognize_gesture(landmarks)

                if gesture_id == 3:
                    print("🖐️ Open Palm Detected - Closing active window")
                    close_recent_window(opencv_hwnd)
                    time.sleep(1.5)
                    continue

                if gesture_id and gesture_id != last_gesture:
                    if current_time - last_action_time >= cooldown_seconds:
                        last_gesture = gesture_id
                        app = applications.get(gesture_id)
                        if app:
                            launch_application(app)
                            last_action_time = current_time
                            cv2.putText(frame, f"Launching: {app}", (10, 60),
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        else:
            last_gesture = None

        cv2.putText(frame, "Show 🖐️ to close latest non-camera window", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
        cv2.putText(frame, "Press 'q' to exit", (10, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (200, 200, 200), 2)
        cv2.imshow("Hand Gesture App Launcher", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
