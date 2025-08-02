import whisper
import os
from config import (
    WHISPER_MODEL_SIZE,
    OUTPUT_DIR
)

def transcribe(input_dir, model_size = WHISPER_MODEL_SIZE, output_dir = OUTPUT_DIR):
    os.system(f"whisper {input_dir} --model {model_size} --output_format srt --language ar --output_dir {output_dir}")

if __name__ == "__main__":
    transcribe(input_dir="data/videoplayback.mp4")
