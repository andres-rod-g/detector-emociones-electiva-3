import os
import sys

# Suppress TensorFlow/OpenCV warnings
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
os.environ["OPENCV_LOG_LEVEL"] = "SILENT"

# Ensure project root is in path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.app import App


def main():
    app = App()
    app.run()


if __name__ == "__main__":
    main()
