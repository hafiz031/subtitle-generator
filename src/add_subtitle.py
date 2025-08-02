import os
from config import OUTPUT_DIR, OUTPUT_FORMAT

def add_subtitle(input_dir, output_dir, mode):

    subtitle_file = f"{os.path.splitext(os.path.split(input_dir)[-1])[0]}.{OUTPUT_FORMAT.lower()}"
    subtitle_path = os.path.join(output_dir, subtitle_file)
    output_file = os.path.join(output_dir, os.path.split(input_dir)[-1])
    
    if mode == "hard":
        cmd = f"ffmpeg -i \"{input_dir}\" -vf subtitles=\"{subtitle_path}\" -c:a copy -map 0:v -map 0:a \"{output_file}\""
    elif mode == "soft":
        # Soft subs require mov_text codec for MP4, or use `-c:s srt` for MKV
        cmd = f"ffmpeg -i \"{input_dir}\" -i \"{subtitle_path}\" -c copy -c:s mov_text \"{output_file}\""

    os.system(cmd)
