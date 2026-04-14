import time
# GUÍA 5 | threading: hilo daemon ejecuta detección sin bloquear el event loop de UI
import threading

from src.core.camera_service import CameraService
from src.core.emotion_detector import EmotionDetector
from src.ui.main_window import MainWindow


class App:
    """Main application orchestrator. Wires services and UI together."""

    UPDATE_INTERVAL_MS = 16  # ~60 FPS for smooth video
    DEFAULT_CAMERA = 2
    MAX_CAMERA_INDEX = 4

    def __init__(self):
        self._camera = CameraService(camera_index=self.DEFAULT_CAMERA)
        self._emotion_detector = EmotionDetector()

        self._window = MainWindow(
            on_close_callback=self._on_close,
            on_camera_change=self._on_camera_change,
        )

        self._last_result = None
        self._last_time = time.time()
        self._fps = 0.0
        self._running = False

        # Detection runs in a background thread
        # GUÍA 5 | Lock: sincroniza acceso al frame compartido entre hilo detección y UI
        self._detect_lock = threading.Lock()
        self._latest_frame = None
        self._detecting = False

    def run(self):
        """Start the application."""
        # GUÍA 6 | Vector: lista de índices de cámara disponibles para selección
        indices = list(range(self.MAX_CAMERA_INDEX + 1))
        self._window.set_camera_options(indices, self._camera.camera_index)

        # GUÍA 6 | Despliegue: verificación de hardware requerido antes de iniciar la sesión
        if not self._camera.start():
            self._window.show_camera_error()
        else:
            self._running = True
            self._start_detection_thread()
            self._schedule_update()

        # GUÍA 5 | Tkinter: event loop y ventana principal de la aplicación
        self._window.mainloop()

    def _start_detection_thread(self):
        """Start the background emotion detection thread."""
        self._detecting = True
        # GUÍA 5 | threading: hilo daemon ejecuta detección sin bloquear el event loop de UI
        thread = threading.Thread(target=self._detection_loop, daemon=True)
        thread.start()

    def _detection_loop(self):
        """Runs in a background thread. Picks up frames and detects emotions."""
        # GUÍA 5 | Loop while: mantiene el hilo de detección activo mientras la app corre
        while self._detecting:
            with self._detect_lock:
                frame = self._latest_frame

            if frame is None:
                time.sleep(0.01)
                # GUÍA 5 | continue: salta el ciclo si no hay frame disponible aún
                continue

            result = self._emotion_detector.detect(frame)

            with self._detect_lock:
                self._last_result = result

            time.sleep(0.02)

    def _on_camera_change(self, camera_index: int):
        """Handle camera switch from the UI button."""
        if camera_index == self._camera.camera_index and self._camera.is_opened():
            return

        self._running = False
        with self._detect_lock:
            self._last_result = None
            self._latest_frame = None

        if self._camera.switch_camera(camera_index):
            self._running = True
            self._last_time = time.time()
            self._fps = 0.0
            self._schedule_update()
        else:
            self._window.show_camera_error()

    def _schedule_update(self):
        """Schedule the next frame update."""
        if self._running:
            self._window.after(self.UPDATE_INTERVAL_MS, self._update_loop)

    def _update_loop(self):
        """Main update cycle: capture frame, read latest result, render."""
        if not self._running:
            return

        frame = self._camera.read_frame()
        if frame is None:
            self._window.show_camera_error()
            self._running = False
            return

        # Send frame to detection thread
        with self._detect_lock:
            self._latest_frame = frame
            result = self._last_result

        # Calculate FPS
        now = time.time()
        delta = now - self._last_time
        if delta > 0:
            self._fps = 0.9 * self._fps + 0.1 * (1.0 / delta)
        self._last_time = now

        self._window.update_frame(frame, result, self._fps)
        self._schedule_update()

    def _on_close(self):
        """Clean up resources on window close."""
        self._running = False
        self._detecting = False
        self._camera.release()
