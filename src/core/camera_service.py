import cv2
import numpy as np


class CameraService:
    """Encapsulates webcam capture via OpenCV."""

    def __init__(self, camera_index: int = 0, width: int = 640, height: int = 480):
        self._camera_index = camera_index
        self._width = width
        self._height = height
        self._cap: cv2.VideoCapture | None = None

    def start(self) -> bool:
        """Open the camera. Returns True if successful."""
        self._cap = cv2.VideoCapture(self._camera_index)
        if not self._cap.isOpened():
            self._cap = None
            return False
        self._cap.set(cv2.CAP_PROP_FRAME_WIDTH, self._width)
        self._cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self._height)
        return True

    def read_frame(self) -> np.ndarray | None:
        """Read a single frame. Returns None on failure."""
        if self._cap is None or not self._cap.isOpened():
            return None
        ret, frame = self._cap.read()
        return frame if ret else None

    def is_opened(self) -> bool:
        return self._cap is not None and self._cap.isOpened()

    def release(self) -> None:
        """Release the camera resource."""
        if self._cap is not None:
            self._cap.release()
            self._cap = None

    def switch_camera(self, camera_index: int) -> bool:
        """Release current camera and open a new one by index."""
        self.release()
        self._camera_index = camera_index
        return self.start()

    @property
    def camera_index(self) -> int:
        return self._camera_index

    @staticmethod
    def list_available(max_index: int = 5) -> list[int]:
        """Probe camera indices and return those that can be opened."""
        # GUÍA 6 | Vector: acumula índices de cámaras que se pueden abrir exitosamente
        available = []
        # GUÍA 5 | Loop for: recorre índices posibles de cámara para detectar las disponibles
        for i in range(max_index):
            cap = cv2.VideoCapture(i)
            if cap.isOpened():
                available.append(i)
                cap.release()
        return available

    def get_resolution(self) -> tuple[int, int]:
        if self._cap is None:
            return (0, 0)
        w = int(self._cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        h = int(self._cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        return (w, h)
