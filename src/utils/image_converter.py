import cv2
import numpy as np
from PIL import Image
from customtkinter import CTkImage


def cv_to_ctk_image(frame: np.ndarray, size: tuple[int, int]) -> CTkImage:
    """Convert an OpenCV BGR frame to a CTkImage."""
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(rgb_frame)
    return CTkImage(light_image=pil_image, dark_image=pil_image, size=size)


def draw_face_box(
    frame: np.ndarray,
    box: tuple[int, int, int, int],
    color: tuple[int, int, int] = (0, 212, 170),
    thickness: int = 2,
) -> np.ndarray:
    """Draw a rounded-corner rectangle around a detected face."""
    x, y, w, h = box
    radius = min(15, w // 6, h // 6)

    # Draw the four straight edges
    cv2.line(frame, (x + radius, y), (x + w - radius, y), color, thickness)
    cv2.line(frame, (x + radius, y + h), (x + w - radius, y + h), color, thickness)
    cv2.line(frame, (x, y + radius), (x, y + h - radius), color, thickness)
    cv2.line(frame, (x + w, y + radius), (x + w, y + h - radius), color, thickness)

    # Draw the four corner arcs
    cv2.ellipse(frame, (x + radius, y + radius), (radius, radius), 180, 0, 90, color, thickness)
    cv2.ellipse(frame, (x + w - radius, y + radius), (radius, radius), 270, 0, 90, color, thickness)
    cv2.ellipse(frame, (x + radius, y + h - radius), (radius, radius), 90, 0, 90, color, thickness)
    cv2.ellipse(frame, (x + w - radius, y + h - radius), (radius, radius), 0, 0, 90, color, thickness)

    return frame
