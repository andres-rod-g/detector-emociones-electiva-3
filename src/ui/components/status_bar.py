from typing import Callable

import customtkinter as ctk

from src.theme import fonts


class StatusBar(ctk.CTkFrame):
    """Bottom status bar showing camera state, FPS and camera switch button."""

    def __init__(self, master, on_camera_change: Callable[[int], None] | None = None, **kwargs):
        super().__init__(master, corner_radius=8, fg_color="#16213e", height=36, **kwargs)

        self._on_camera_change = on_camera_change
        self._available_indices: list[int] = []
        self._current_index = 0

        self.grid_columnconfigure(1, weight=1)

        self._camera_dot = ctk.CTkLabel(
            self, text="●", font=fonts.CAPTION, text_color="#E74C3C", width=20
        )
        self._camera_dot.grid(row=0, column=0, padx=(12, 4), pady=6)

        self._status_label = ctk.CTkLabel(
            self, text="Cámara desconectada", font=fonts.CAPTION, text_color="#B0B0B0"
        )
        self._status_label.grid(row=0, column=1, sticky="w", pady=6)

        self._fps_label = ctk.CTkLabel(
            self, text="0 FPS", font=fonts.CAPTION, text_color="#B0B0B0"
        )
        self._fps_label.grid(row=0, column=2, padx=(0, 8), pady=6)

        self._camera_label = ctk.CTkLabel(
            self, text="Cámara: 0", font=fonts.CAPTION, text_color="#B0B0B0"
        )
        self._camera_label.grid(row=0, column=3, padx=(8, 4), pady=6)

        self._switch_btn = ctk.CTkButton(
            self,
            text="Cambiar ⟳",
            width=90,
            height=24,
            font=fonts.CAPTION,
            fg_color="#533483",
            hover_color="#6a42a0",
            corner_radius=6,
            command=self._on_switch_click,
        )
        self._switch_btn.grid(row=0, column=4, padx=(0, 12), pady=6)

    def set_camera_options(self, indices: list[int], current: int):
        """Store available camera indices and set current."""
        self._available_indices = indices
        self._current_index = current
        self._camera_label.configure(text=f"Cámara: {current}")

    def _on_switch_click(self):
        """Cycle to the next available camera index."""
        if not self._available_indices or not self._on_camera_change:
            return

        try:
            pos = self._available_indices.index(self._current_index)
            next_pos = (pos + 1) % len(self._available_indices)
        except ValueError:
            next_pos = 0

        next_index = self._available_indices[next_pos]
        self._current_index = next_index
        self._camera_label.configure(text=f"Cámara: {next_index}")
        self._on_camera_change(next_index)

    def update_status(self, camera_active: bool, fps: float = 0.0):
        """Update the status bar indicators."""
        if camera_active:
            self._camera_dot.configure(text_color="#00D4AA")
            self._status_label.configure(text="Cámara activa", text_color="#FFFFFF")
        else:
            self._camera_dot.configure(text_color="#E74C3C")
            self._status_label.configure(text="Cámara desconectada", text_color="#B0B0B0")

        self._fps_label.configure(text=f"{fps:.0f} FPS")
