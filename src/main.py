from transcriber import transcribe
from translator import translate
from utils import generate_datetime_string
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Transcribe and subtitle a video")
    parser.add_argument("--input", type=str, required=True, help="Input audio or video file")
    parser.add_argument("--input_lang", type=str, required=True, help="Language code of the audio")
    parser.add_argument("--translate", type=str, default=True, help="Whether to translate or transcribe.")
    args = parser.parse_args()

    print(f"Processing {args.input} in language {args.input_lang}")

    output_id = generate_datetime_string()

    if args.translate == True:
        translate(input_dir=args.input, source_language=args.input_lang, output_id=output_id)
    else:
        transcribe(input_dir=args.input, source_language=args.input_lang, output_id=output_id)

    
