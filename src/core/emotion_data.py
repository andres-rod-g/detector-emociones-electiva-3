from dataclasses import dataclass
from src.theme.colors import EMOTION_COLORS, EMOTION_EMOJIS


@dataclass(frozen=True)
class EmotionInfo:
    key: str
    name: str
    description: str
    color: str
    emoji: str


# GUÍA 5 | Diccionario: catálogo de emociones con clave string y objeto EmotionInfo como valor
_EMOTION_CATALOG: dict[str, EmotionInfo] = {
    "neutral": EmotionInfo(
        key="neutral",
        name="Neutral",
        description="Tu rostro muestra una expresión tranquila y relajada, sin emociones marcadas.",
        color=EMOTION_COLORS["neutral"],
        emoji=EMOTION_EMOJIS["neutral"],
    ),
    "happiness": EmotionInfo(
        key="happiness",
        name="Felicidad",
        description="Se detecta una sonrisa genuina. La felicidad activa los músculos alrededor de los ojos y la boca.",
        color=EMOTION_COLORS["happiness"],
        emoji=EMOTION_EMOJIS["happiness"],
    ),
    "surprise": EmotionInfo(
        key="surprise",
        name="Sorpresa",
        description="Cejas levantadas y boca abierta. La sorpresa es la emoción más breve y puede ser positiva o negativa.",
        color=EMOTION_COLORS["surprise"],
        emoji=EMOTION_EMOJIS["surprise"],
    ),
    "sadness": EmotionInfo(
        key="sadness",
        name="Tristeza",
        description="Se percibe una expresión de melancolía. Los párpados caen y las comisuras de los labios descienden.",
        color=EMOTION_COLORS["sadness"],
        emoji=EMOTION_EMOJIS["sadness"],
    ),
    "anger": EmotionInfo(
        key="anger",
        name="Enojo",
        description="Ceño fruncido y mandíbula tensa. El enojo prepara al cuerpo para una respuesta de lucha.",
        color=EMOTION_COLORS["anger"],
        emoji=EMOTION_EMOJIS["anger"],
    ),
    "disgust": EmotionInfo(
        key="disgust",
        name="Disgusto",
        description="Nariz arrugada y labio superior levantado. El disgusto es una respuesta de rechazo instintiva.",
        color=EMOTION_COLORS["disgust"],
        emoji=EMOTION_EMOJIS["disgust"],
    ),
    "fear": EmotionInfo(
        key="fear",
        name="Miedo",
        description="Ojos muy abiertos y cejas elevadas. El miedo activa la respuesta de huida del cuerpo.",
        color=EMOTION_COLORS["fear"],
        emoji=EMOTION_EMOJIS["fear"],
    ),
}

# GUÍA 6 | Vector: lista ordenada de claves de emoción para recorrido secuencial
EMOTION_KEYS = list(_EMOTION_CATALOG.keys())


def get_emotion_info(emotion_key: str) -> EmotionInfo:
    """Return info for a given emotion key. Falls back to neutral."""
    return _EMOTION_CATALOG.get(emotion_key, _EMOTION_CATALOG["neutral"])


def get_all_emotions() -> list[EmotionInfo]:
    """Return all emotion info entries."""
    # GUÍA 6 | Vector: retorna todas las emociones como lista para recorrido en panel
    return list(_EMOTION_CATALOG.values())
