"""Download the FERPlus ONNX emotion classification model."""

import os
import urllib.request
import shutil

MODEL_URLS = [
    "https://huggingface.co/onnxmodelzoo/emotion-ferplus-8/resolve/main/emotion-ferplus-8.onnx",
    "https://github.com/onnx/models/raw/main/validated/vision/"
    "body_analysis/emotion_ferplus/model/emotion-ferplus-8.onnx",
]
MODEL_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "models")
MODEL_PATH = os.path.join(MODEL_DIR, "emotion-ferplus-8.onnx")


def download():
    os.makedirs(MODEL_DIR, exist_ok=True)

    if os.path.exists(MODEL_PATH) and os.path.getsize(MODEL_PATH) > 1_000_000:
        size_mb = os.path.getsize(MODEL_PATH) / (1024 * 1024)
        print(f"El modelo ya existe en: {MODEL_PATH} ({size_mb:.1f} MB)")
        return

    # Remove partial downloads
    if os.path.exists(MODEL_PATH):
        os.remove(MODEL_PATH)

    for url in MODEL_URLS:
        try:
            print(f"Descargando modelo FERPlus ONNX (~35 MB)...")
            print(f"Desde: {url}")
            tmp_path = MODEL_PATH + ".tmp"
            urllib.request.urlretrieve(url, tmp_path)
            shutil.move(tmp_path, MODEL_PATH)
            size_mb = os.path.getsize(MODEL_PATH) / (1024 * 1024)
            print(f"Modelo descargado exitosamente ({size_mb:.1f} MB)")
            print(f"Ubicación: {MODEL_PATH}")
            return
        except Exception as e:
            print(f"Error con esta URL: {e}")
            if os.path.exists(tmp_path):
                os.remove(tmp_path)
            continue

    print("ERROR: No se pudo descargar el modelo de ninguna fuente.")
    print("Descárgalo manualmente y colócalo en: " + MODEL_PATH)


if __name__ == "__main__":
    download()
