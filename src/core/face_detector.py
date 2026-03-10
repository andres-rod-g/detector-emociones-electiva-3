import cv2
import numpy as np


class FaceDetector:
    """Detects faces using OpenCV Haar Cascade (included with OpenCV)."""

    def __init__(self, scale_factor: float = 1.3, min_neighbors: int = 5, min_size: int = 48):
        cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        self._cascade = cv2.CascadeClassifier(cascade_path)
        self._scale_factor = scale_factor
        self._min_neighbors = min_neighbors
        self._min_size = (min_size, min_size)

    def detect(self, frame: np.ndarray) -> list[tuple[int, int, int, int]]:
        """Detect faces in a BGR frame. Downscales internally for speed."""
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Downscale for faster detection
        h, w = gray.shape
        max_dim = 320
        scale = 1.0
        if max(h, w) > max_dim:
            scale = max_dim / max(h, w)
            gray = cv2.resize(gray, (int(w * scale), int(h * scale)))

        gray = cv2.equalizeHist(gray)

        faces = self._cascade.detectMultiScale(
            gray,
            scaleFactor=self._scale_factor,
            minNeighbors=self._min_neighbors,
            minSize=self._min_size,
            flags=cv2.CASCADE_SCALE_IMAGE,
        )

        if len(faces) == 0:
            return []

        # Scale coordinates back to original frame size
        inv = 1.0 / scale
        return [(int(x * inv), int(y * inv), int(w_ * inv), int(h_ * inv)) for (x, y, w_, h_) in faces]

    def get_largest_face(self, faces: list[tuple[int, int, int, int]]) -> tuple[int, int, int, int] | None:
        """Return the largest face by area, or None if list is empty."""
        if not faces:
            return None
        return max(faces, key=lambda f: f[2] * f[3])
