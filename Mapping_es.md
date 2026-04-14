# Mapping Académico — EduEmotion

## GUÍA 5: Definición del Stack Tecnológico

| Concepto | Archivo | Línea |
|---|---|---|
| CustomTkinter (UI moderna) | `src/ui/main_window.py` | 1 |
| Tkinter event loop / ventana | `src/app.py` | 51 |
| Pillow frame→CTkImage | `src/utils/image_converter.py` | 13 |
| OpenCV apertura webcam | `src/core/camera_service.py` | 16 |
| OpenCV preprocesamiento frame | `src/core/face_detector.py` | 18 |
| Haar Cascade detección rostros | `src/core/face_detector.py` | 10 |
| OpenCV dibujo caja facial | `src/utils/image_converter.py` | 29 |
| FER clasificación emocional | `src/core/emotion_detector.py` | 8 |
| TensorFlow backend inferencia | `src/core/emotion_detector.py` | 4 |
| FERPlus ONNX modelo | `src/core/emotion_detector.py` | 37 |
| threading daemon detección | `src/app.py` | 57 |
| threading.Lock sincronización | `src/app.py` | 32 |
| urllib descarga modelo HTTPS | `download_model.py` | 4 |
| shutil gestión archivos modelo | `download_model.py` | 6 |
| dataclass EmotionResult/Info | `src/core/emotion_detector.py` | 12 |

## GUÍA 6: Plan de Despliegue y Gobernanza

| Concepto | Archivo | Línea |
|---|---|---|
| Descarga automática modelo (primer arranque) | `download_model.py` | 24 |
| Verificación webcam disponible | `src/app.py` | 43 |

## GUÍA 7: Diseño de Infraestructura de Persistencia y Seguridad Cloud

| Concepto | Archivo | Línea |
|---|---|---|
| Cifrado en tránsito (HTTPS/TLS) | `download_model.py` | 12 |
