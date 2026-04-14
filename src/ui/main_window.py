# GUÍA 5 | CustomTkinter: widgets modernos de la interfaz gráfica del sistema
import customtkinter as ctk

from src.core.emotion_detector import EmotionResult
from src.ui.components.video_display import VideoDisplay
from src.ui.components.emotion_panel import EmotionPanel
from src.ui.components.status_bar import StatusBar

import numpy as np


class MainWindow(ctk.CTk):
    """Main application window with video feed and emotion panel layout."""

    APP_TITLE = "Detector de Emociones"
    MIN_WIDTH = 1100
    MIN_HEIGHT = 650

    def __init__(self, on_close_callback=None, on_camera_change=None):
        super().__init__()

        self._on_close_callback = on_close_callback
        self._on_camera_change = on_camera_change

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.title(self.APP_TITLE)
        self.minsize(self.MIN_WIDTH, self.MIN_HEIGHT)
        self.geometry(f"{self.MIN_WIDTH}x{self.MIN_HEIGHT}")
        self.configure(fg_color="#1a1a2e")

        self.protocol("WM_DELETE_WINDOW", self._handle_close)

        self._build_layout()

    def _build_layout(self):
        """Create the main two-column layout."""
        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)

        # Left column: video feed
        self.video_display = VideoDisplay(self, display_width=640, display_height=480)
        self.video_display.grid(row=0, column=0, sticky="nsew", padx=(15, 8), pady=(15, 8))

        # Right column: emotion panel
        self.emotion_panel = EmotionPanel(self)
        self.emotion_panel.grid(row=0, column=1, sticky="nsew", padx=(8, 15), pady=(15, 8))

        # Bottom: status bar spanning both columns
        self.status_bar = StatusBar(self, on_camera_change=self._on_camera_change)
        self.status_bar.grid(row=1, column=0, columnspan=2, sticky="ew", padx=15, pady=(0, 15))

    def update_frame(
        self,
        frame: np.ndarray,
        emotion_result: EmotionResult | None,
        fps: float = 0.0,
    ):
        """Update all UI components with new frame data."""
        face_box = emotion_result.face_box if emotion_result else None
        self.video_display.update_image(frame, face_box=face_box)
        self.emotion_panel.update_emotion(emotion_result)
        self.status_bar.update_status(camera_active=True, fps=fps)

    def set_camera_options(self, indices: list[int], current: int):
        """Populate camera selector in the status bar."""
        self.status_bar.set_camera_options(indices, current)

    def show_camera_error(self):
        """Display camera error state."""
        self.video_display.show_placeholder("❌  No se pudo acceder a la cámara")
        self.status_bar.update_status(camera_active=False)

    def _handle_close(self):
        if self._on_close_callback:
            self._on_close_callback()
        self.destroy()
