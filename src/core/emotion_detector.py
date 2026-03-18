import os
from dataclasses import dataclass

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

import numpy as np
from fer.fer import FER


@dataclass
class EmotionResult:
    dominant_emotion: str
    confidence: float
    all_emotions: dict[str, float]
    face_box: tuple[int, int, int, int]


# GUÍA 5 | Diccionario: mapea claves de FER a claves internas del sistema de emociones
_FER_KEY_MAP = {
    "angry": "anger",
    "disgust": "disgust",
    "fear": "fear",
    "happy": "happiness",
    "sad": "sadness",
    "surprise": "surprise",
    "neutral": "neutral",
}


class EmotionDetector:
    """Detects faces and classifies emotions using the FER library."""

    def __init__(self):
        self._detector = FER(mtcnn=False)

    def detect(self, frame: np.ndarray) -> EmotionResult | None:
        """Detect the dominant face and its emotions in a BGR frame."""
        results = self._detector.detect_emotions(frame)

        if not results:
            return None

        # Pick the face with the highest confidence on its dominant emotion
        best = max(results, key=lambda r: max(r["emotions"].values()))

        box = best["box"]
        x, y, w, h = int(box[0]), int(box[1]), int(box[2]), int(box[3])

        raw_emotions = best["emotions"]
        # GUÍA 5 | Diccionario: construye diccionario de emociones mapeadas con sus confianzas
        mapped_emotions = {
            _FER_KEY_MAP.get(k, k): float(v)
            for k, v in raw_emotions.items()
        }

        dominant_key = max(raw_emotions, key=raw_emotions.get)
        dominant_mapped = _FER_KEY_MAP.get(dominant_key, dominant_key)
        confidence = float(raw_emotions[dominant_key])

        return EmotionResult(
            dominant_emotion=dominant_mapped,
            confidence=confidence,
            all_emotions=mapped_emotions,
            face_box=(x, y, w, h),
        )
