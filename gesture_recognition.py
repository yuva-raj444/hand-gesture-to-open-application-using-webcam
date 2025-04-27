from utils import distance

# Recognize gesture based on landmarks
def recognize_gesture(landmarks):
    thumb_tip = landmarks[4]
    index_tip = landmarks[8]
    middle_tip = landmarks[12]
    ring_tip = landmarks[16]
    pinky_tip = landmarks[20]
    wrist = landmarks[0]

    thumb_dist = distance(thumb_tip, wrist)
    index_dist = distance(index_tip, wrist)
    middle_dist = distance(middle_tip, wrist)
    ring_dist = distance(ring_tip, wrist)
    pinky_dist = distance(pinky_tip, wrist)

    fingers = [
        thumb_tip.x > landmarks[3].x,
        index_tip.y < landmarks[6].y,
        middle_tip.y < landmarks[10].y,
        ring_tip.y < landmarks[14].y,
        pinky_tip.y < landmarks[18].y
    ]

    if fingers == [1, 0, 0, 0, 0] and thumb_dist > 0.05:
        return 1
    if fingers == [0, 1, 1, 0, 0] and index_dist > 0.05 and middle_dist > 0.05:
        return 2
    if fingers == [1, 1, 1, 1, 1] and index_dist > 0.07 and middle_dist > 0.07:
        return 3
    if fingers == [0, 0, 0, 0, 0] and thumb_dist < 0.05:
        return 4
    if fingers == [1, 0, 0, 0, 1] and pinky_dist > 0.05:
        return 5
    if fingers == [0, 1, 0, 0, 0]:
        return 6
    if fingers == [0, 1, 1, 0, 1]:
        return 7
    if fingers == [1, 1, 0, 0, 1]:
        return 8
    if fingers == [0, 0, 1, 1, 1]:
        return 9
    if fingers == [0, 0, 0, 1, 1]:
        return 10
    return None
