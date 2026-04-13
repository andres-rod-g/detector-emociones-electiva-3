# Academic Mapping — EduEmotion

## GUIDE 5: Iterative Structures and Dictionaries

| Concept | File | Line |
|---|---|---|
| `while` loop | `src/app.py` | 57 |
| `continue` (null frame in thread) | `src/app.py` | 64 |
| `for` loop (camera indices) | `src/core/camera_service.py` | 54 |
| Dictionary (FER → internal key mapping) | `src/core/emotion_detector.py` | 18 |
| Dictionary (mapped emotions with confidence) | `src/core/emotion_detector.py` | 50 |
| Dictionary (emotion catalog) | `src/core/emotion_data.py` | 14 |
| `for` loop (scale face coordinates) | `src/core/face_detector.py` | 42 |
| Dictionary (emotion cards by key) | `src/ui/components/emotion_panel.py` | 54 |
| `for` loop (build panel cards) | `src/ui/components/emotion_panel.py` | 56 |
| `for` loop (update emotion bars) | `src/ui/components/emotion_panel.py` | 92 |
| `for` loop (reset confidences on no face) | `src/ui/components/emotion_panel.py` | 111 |
| `for` loop (model download URLs) | `download_model.py` | 28 |
| `continue` (failed download URL) | `download_model.py` | 44 |

## GUIDE 6: Arrays and Matrices (Multidimensional Structures)

| Concept | File | Line |
|---|---|---|
| Vector (download URLs) | `download_model.py` | 7 |
| Vector (available camera indices) | `src/app.py` | 37 |
| Vector (accumulation of opened cameras) | `src/core/camera_service.py` | 53 |
| Vector (emotion keys for iteration) | `src/core/emotion_data.py` | 67 |
| Vector (EmotionInfo list for panel) | `src/core/emotion_data.py` | 78 |
| Dimension validation (`len` on faces) | `src/core/face_detector.py` | 37 |
| Vector (camera indices in status bar) | `src/ui/components/status_bar.py` | 15 |
| Dimension validation (`len` camera cycle) | `src/ui/components/status_bar.py` | 67 |

## GUIDE 7: Persistence Infrastructure and Cloud Security Design

| Concept | File | Line |
|---|---|---|
| Local storage (offline-first) | N/A | — |
| Sync queue | N/A | — |
| HTTPS cloud synchronization | N/A | — |
| Encryption at rest (AES-256) | N/A | — |
| Encryption in transit (HTTPS/TLS) | `download_model.py` | 9 |
| JWT authentication | N/A | — |
| Role/permission management | N/A | — |
| Reconnection handling | N/A | — |
