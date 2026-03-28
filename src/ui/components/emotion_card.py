import customtkinter as ctk

from src.theme import fonts
from src.theme.colors import EMOTION_COLORS, EMOTION_EMOJIS


class EmotionCard(ctk.CTkFrame):
    """Displays a single emotion with emoji, name, confidence bar and percentage."""

    def __init__(self, master, emotion_key: str = "neutral", highlight: bool = False, **kwargs):
        super().__init__(master, corner_radius=12, fg_color="#16213e", **kwargs)

        self._highlight = highlight
        self._emotion_key = emotion_key

        if highlight:
            self._build_highlight_layout()
        else:
            self._build_compact_layout()

    def _build_highlight_layout(self):
        """Large card for the dominant emotion."""
        self.configure(fg_color="#1a2745", border_width=2, border_color="#2a2a4a")

        self._emoji_label = ctk.CTkLabel(
            self, text="😐", font=fonts.EMOJI_LARGE, text_color="#FFFFFF"
        )
        self._emoji_label.pack(pady=(20, 5))

        self._name_label = ctk.CTkLabel(
            self, text="Neutral", font=fonts.SUBTITLE, text_color="#FFFFFF"
        )
        self._name_label.pack(pady=(0, 5))

        self._confidence_label = ctk.CTkLabel(
            self, text="0%", font=fonts.HEADING, text_color="#B0B0B0"
        )
        self._confidence_label.pack(pady=(0, 5))

        self._progress_bar = ctk.CTkProgressBar(
            self, width=200, height=8, corner_radius=4,
            fg_color="#2a2a4a", progress_color="#95A5A6"
        )
        self._progress_bar.pack(pady=(0, 5))
        self._progress_bar.set(0)

        self._description_label = ctk.CTkLabel(
            self, text="", font=fonts.CAPTION, text_color="#B0B0B0",
            wraplength=220, justify="center"
        )
        self._description_label.pack(pady=(5, 15), padx=15)

    def _build_compact_layout(self):
        """Small row card for the emotion list."""
        self.configure(fg_color="transparent")

        row = ctk.CTkFrame(self, fg_color="transparent")
        row.pack(fill="x", padx=8, pady=3)
        row.grid_columnconfigure(2, weight=1)

        self._emoji_label = ctk.CTkLabel(
            row, text="😐", font=fonts.EMOJI_SMALL, width=30
        )
        self._emoji_label.grid(row=0, column=0, padx=(0, 6))

        self._name_label = ctk.CTkLabel(
            row, text="Neutral", font=fonts.CAPTION, text_color="#B0B0B0",
            width=75, anchor="w"
        )
        self._name_label.grid(row=0, column=1, padx=(0, 6))

        self._progress_bar = ctk.CTkProgressBar(
            row, height=6, corner_radius=3,
            fg_color="#2a2a4a", progress_color="#95A5A6"
        )
        self._progress_bar.grid(row=0, column=2, sticky="ew", padx=(0, 6))
        self._progress_bar.set(0)

        self._confidence_label = ctk.CTkLabel(
            row, text="0%", font=fonts.PERCENTAGE, text_color="#B0B0B0", width=40
        )
        self._confidence_label.grid(row=0, column=3)

        self._description_label = None

    def update(self, emotion_key: str, name: str, confidence: float, description: str = ""):
        """Update the card with new emotion data."""
        color = EMOTION_COLORS.get(emotion_key, "#95A5A6")
        emoji = EMOTION_EMOJIS.get(emotion_key, "😐")

        self._emoji_label.configure(text=emoji)
        self._name_label.configure(text=name)
        self._confidence_label.configure(text=f"{confidence:.0%}")
        self._progress_bar.configure(progress_color=color)
        self._progress_bar.set(confidence)

        if self._highlight:
            self.configure(border_color=color)
            self._name_label.configure(text_color=color)
            if self._description_label:
                self._description_label.configure(text=description)
