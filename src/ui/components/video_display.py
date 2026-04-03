import numpy as np
import customtkinter as ctk

from src.theme import fonts
from src.utils.image_converter import cv_to_ctk_image, draw_face_box
from src.theme.colors import UI_COLORS


class VideoDisplay(ctk.CTkFrame):
    """Widget that displays the webcam feed with face detection overlay."""

    def __init__(self, master, display_width: int = 640, display_height: int = 480, **kwargs):
        super().__init__(master, corner_radius=12, fg_color="#16213e", **kwargs)

        self._display_size = (display_width, display_height)

        self._video_label = ctk.CTkLabel(self, text="")
        self._video_label.pack(padx=10, pady=10)

        self._placeholder_label = ctk.CTkLabel(
            self, text="📷  Conectando cámara...",
            font=fonts.SUBTITLE, text_color="#B0B0B0"
        )
        self._placeholder_label.pack(expand=True)

        self._showing_video = False

    def update_image(
        self,
        frame: np.ndarray,
        face_box: tuple[int, int, int, int] | None = None,
        face_color: tuple[int, int, int] = UI_COLORS["face_box_bg"],
    ):
        """Update the displayed frame, optionally drawing a face box."""
        if not self._showing_video:
            self._placeholder_label.pack_forget()
            self._showing_video = True

        if face_box is not None:
            frame = draw_face_box(frame.copy(), face_box, color=face_color)

        ctk_image = cv_to_ctk_image(frame, self._display_size)
        self._video_label.configure(image=ctk_image)
        self._video_label._image = ctk_image  # prevent garbage collection

    def show_placeholder(self, text: str = "📷  Conectando cámara..."):
        """Show a placeholder message instead of video."""
        self._video_label.configure(image=None)
        self._placeholder_label.configure(text=text)
        self._placeholder_label.pack(expand=True)
        self._showing_video = False
