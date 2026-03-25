# Mapping Académico — EduEmotion

## GUÍA 5: Estructuras Iterativas y Diccionarios

| Concepto | Archivo | Línea |
|---|---|---|
| Loop `while` | `src/app.py` | 57 |
| `continue` (frame nulo en hilo) | `src/app.py` | 64 |
| Loop `for` (índices de cámara) | `src/core/camera_service.py` | 54 |
| Diccionario (mapeo FER → clave interna) | `src/core/emotion_detector.py` | 18 |
| Diccionario (emociones mapeadas con confianza) | `src/core/emotion_detector.py` | 50 |
| Diccionario (catálogo de emociones) | `src/core/emotion_data.py` | 14 |
| Loop `for` (escalar coordenadas de rostros) | `src/core/face_detector.py` | 42 |
| Diccionario (tarjetas de emoción por clave) | `src/ui/components/emotion_panel.py` | 54 |
| Loop `for` (crear tarjetas en panel) | `src/ui/components/emotion_panel.py` | 56 |
| Loop `for` (actualizar barras de emoción) | `src/ui/components/emotion_panel.py` | 92 |
| Loop `for` (resetear confianzas sin rostro) | `src/ui/components/emotion_panel.py` | 111 |
| Loop `for` (URLs de descarga del modelo) | `download_model.py` | 28 |
| `continue` (URL de descarga fallida) | `download_model.py` | 44 |

## GUÍA 6: Arrays y Matrices (Estructuras Multidimensionales)

| Concepto | Archivo | Línea |
|---|---|---|
| Vector (URLs de descarga) | `download_model.py` | 7 |
| Vector (índices de cámara disponibles) | `src/app.py` | 37 |
| Vector (acumulación de cámaras abiertas) | `src/core/camera_service.py` | 53 |
| Vector (claves de emoción para recorrido) | `src/core/emotion_data.py` | 67 |
| Vector (lista de EmotionInfo para panel) | `src/core/emotion_data.py` | 78 |
| Validación de dimensión (`len` rostros) | `src/core/face_detector.py` | 37 |
| Vector (índices de cámara en status bar) | `src/ui/components/status_bar.py` | 15 |
| Validación de dimensión (`len` cámaras ciclo) | `src/ui/components/status_bar.py` | 67 |
