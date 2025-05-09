"""
Utilitas untuk efek visual dan tampilan instruksi.
"""
import cv2

def show_instruction(frame, letter):
    """
    Tampilkan instruksi huruf saat ini ke frame.
    """
    cv2.putText(frame, f'Tunjukkan huruf: {letter}', (50, 50), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

def show_success_effect(frame):
    """
    Tampilkan efek jika gesture berhasil dikenali.
    """
    cv2.putText(frame, 'Benar!', (200, 240), 
                cv2.FONT_HERSHEY_DUPLEX, 2, (0, 255, 0), 3)
