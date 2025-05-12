# streamlit_app.py   (loader público)

import os
from pathlib import Path

# 1) Carpeta binarios
os.environ["PLAYWRIGHT_BROWSERS_PATH"] = (
    Path(__file__).resolve().parent / "playwright-browsers"   # ← .resolve()
).as_posix()

# 2) App
from ifoodextractor.streamlit_entry import main as run

if __name__ == "__main__":
    run()