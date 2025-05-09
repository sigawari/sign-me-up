"""
Sign Me Up! Belajar Abjad SIBI
Main program untuk menjalankan edukasi interaktif SIBI dengan MediaPipe.
"""

import cv2
from hand_gesture_detector import detect_hand_sign
from sibi_mapping import get_expected_gesture
from utils import show_success_effect, show_instruction

def main():
    cap = cv2.VideoCapture(0)
    current_letter = 'A'

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        detected_gesture = detect_hand_sign(frame)
        expected_gesture = get_expected_gesture(current_letter)

        show_instruction(frame, current_letter)

        if detected_gesture == expected_gesture:
            show_success_effect(frame)
            current_letter = chr(ord(current_letter) + 1) if current_letter != 'Z' else 'A'

        cv2.imshow('Sign Me Up!', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
