import os
from config import OUTPUT_DIR, OUTPUT_FORMAT

def add_subtitle(input_dir, output_dir):

    subtitle_file = f"{os.path.splitext(os.path.split(input_dir)[-1])[0]}.{OUTPUT_FORMAT.lower()}"
    subtitle_path = os.path.join(output_dir, subtitle_file)
    output_file = os.path.join(output_dir, os.path.split(input_dir)[-1])

    os.system(f"ffmpeg -i {input_dir} \
            -vf subtitles={subtitle_path} \
            {output_file}")
