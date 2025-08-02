import whisper
import os
from config import (
    WHISPER_MODEL_SIZE,
    OUTPUT_FORMAT,
    OUTPUT_DIR
)

def transcribe(input_dir, 
            source_language, 
            output_id,
            model_size = WHISPER_MODEL_SIZE, 
            output_format = OUTPUT_FORMAT):
    
    os.system(f"whisper {input_dir} --model {model_size} --output_format {output_format} --language {source_language} --output_dir {os.path.join(OUTPUT_DIR, output_id)}")
