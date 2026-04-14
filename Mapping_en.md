# Academic Mapping — EduEmotion

## GUIDE 5: Technology Stack Definition

| Concept | File | Line |
|---|---|---|
| CustomTkinter (modern UI) | `src/ui/main_window.py` | 1 |
| Tkinter event loop / main window | `src/app.py` | 51 |
| Pillow frame→CTkImage | `src/utils/image_converter.py` | 13 |
| OpenCV webcam open | `src/core/camera_service.py` | 16 |
| OpenCV frame preprocessing | `src/core/face_detector.py` | 18 |
| Haar Cascade face detection | `src/core/face_detector.py` | 10 |
| OpenCV face bounding box | `src/utils/image_converter.py` | 29 |
| FER emotion classification | `src/core/emotion_detector.py` | 8 |
| TensorFlow inference backend | `src/core/emotion_detector.py` | 4 |
| FERPlus ONNX model | `src/core/emotion_detector.py` | 37 |
| threading daemon detection | `src/app.py` | 57 |
| threading.Lock synchronization | `src/app.py` | 32 |
| urllib HTTPS model download | `download_model.py` | 4 |
| shutil model file management | `download_model.py` | 6 |
| dataclass EmotionResult/Info | `src/core/emotion_detector.py` | 12 |

## GUIDE 6: Deployment Plan and Governance

| Concept | File | Line |
|---|---|---|
| Auto model download (first run) | `download_model.py` | 24 |
| Webcam availability check | `src/app.py` | 43 |

## GUIDE 7: Persistence Infrastructure and Cloud Security Design

| Concept | File | Line |
|---|---|---|
| Encryption in transit (HTTPS/TLS) | `download_model.py` | 12 |
