"""
Modul pendeteksi gesture tangan menggunakan MediaPipe.
"""
import mediapipe as mp
import cv2

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1)

def detect_hand_sign(frame):
    """
    Deteksi gesture tangan dari frame.
    :param frame: Frame video (np.array)
    :return: ID gesture (misal 'A', 'B', dst.)
    """
    # TODO: implementasi sesuai mapping gesture SIBI
    return 'A'  # placeholder
