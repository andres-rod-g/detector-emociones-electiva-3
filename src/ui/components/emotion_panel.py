import customtkinter as ctk

from src.core.emotion_data import get_emotion_info, get_all_emotions
from src.core.emotion_detector import EmotionResult
from src.theme import fonts
from src.ui.components.emotion_card import EmotionCard


class EmotionPanel(ctk.CTkFrame):
    """Right-side panel showing detected emotion info and all emotion scores."""

    def __init__(self, master, **kwargs):
        super().__init__(master, corner_radius=12, fg_color="#1a1a2e", **kwargs)

        self._build_header()
        self._build_dominant_card()
        self._build_separator()
        self._build_emotion_list()
        self._build_no_face_label()

    def _build_header(self):
        header = ctk.CTkLabel(
            self, text="Detector de Emociones",
            font=fonts.TITLE, text_color="#FFFFFF"
        )
        header.pack(pady=(20, 5), padx=20)

        subtitle = ctk.CTkLabel(
            self, text="Análisis facial en tiempo real",
            font=fonts.CAPTION, text_color="#B0B0B0"
        )
        subtitle.pack(pady=(0, 15), padx=20)

    def _build_dominant_card(self):
        self._dominant_card = EmotionCard(self, highlight=True)
        self._dominant_card.pack(fill="x", padx=15, pady=(0, 10))

    def _build_separator(self):
        sep_label = ctk.CTkLabel(
            self, text="Todas las emociones",
            font=fonts.HEADING, text_color="#B0B0B0"
        )
        sep_label.pack(pady=(10, 5), padx=20, anchor="w")

        separator = ctk.CTkFrame(self, height=1, fg_color="#2a2a4a")
        separator.pack(fill="x", padx=20, pady=(0, 5))

    def _build_emotion_list(self):
        self._scroll_frame = ctk.CTkScrollableFrame(
            self, fg_color="transparent", corner_radius=0
        )
        self._scroll_frame.pack(fill="both", expand=True, padx=10, pady=(0, 10))

        # GUÍA 5 | Diccionario: almacena tarjetas de emoción indexadas por clave de emoción
        self._emotion_cards: dict[str, EmotionCard] = {}
        # GUÍA 5 | Loop for: recorre todas las emociones para crear sus tarjetas en el panel
        for emotion_info in get_all_emotions():
            card = EmotionCard(self._scroll_frame, emotion_key=emotion_info.key, highlight=False)
            card.pack(fill="x", pady=1)
            card.update(
                emotion_key=emotion_info.key,
                name=emotion_info.name,
                confidence=0.0,
            )
            self._emotion_cards[emotion_info.key] = card

    def _build_no_face_label(self):
        self._no_face_label = ctk.CTkLabel(
            self, text="No se detecta ningún rostro",
            font=fonts.BODY, text_color="#666666"
        )
        # Hidden by default; shown when no face detected

    def update_emotion(self, result: EmotionResult | None):
        """Update the panel with a new emotion detection result."""
        if result is None:
            self._show_no_face()
            return

        self._no_face_label.pack_forget()

        # Update dominant emotion card
        info = get_emotion_info(result.dominant_emotion)
        self._dominant_card.update(
            emotion_key=result.dominant_emotion,
            name=info.name,
            confidence=result.confidence,
            description=info.description,
        )

        # Update all emotion bars
        # GUÍA 5 | Loop for: recorre el diccionario de tarjetas para actualizar cada barra de emoción
        for key, card in self._emotion_cards.items():
            emotion_info = get_emotion_info(key)
            confidence = result.all_emotions.get(key, 0.0)
            card.update(
                emotion_key=key,
                name=emotion_info.name,
                confidence=confidence,
            )

    def _show_no_face(self):
        """Show placeholder when no face is detected."""
        info = get_emotion_info("neutral")
        self._dominant_card.update(
            emotion_key="neutral",
            name="Sin rostro",
            confidence=0.0,
            description="Acerca tu rostro a la cámara para comenzar el análisis.",
        )
        # GUÍA 5 | Loop for: recorre tarjetas para resetear confianzas cuando no hay rostro
        for key, card in self._emotion_cards.items():
            emotion_info = get_emotion_info(key)
            card.update(emotion_key=key, name=emotion_info.name, confidence=0.0)
