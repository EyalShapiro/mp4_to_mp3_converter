import os

from pydub import AudioSegment


class VideoToAudioConverter:
    @staticmethod
    def convert_folder(input_folder: str, output_folder: str):
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        for filename in os.listdir(input_folder):
            if filename.lower().endswith(".mp4"):
                input_path = os.path.join(input_folder, filename)
                output_file = os.path.splitext(filename)[0] + ".mp3"
                output_path = os.path.join(output_folder, output_file)
                VideoToAudioConverter.convert_file(input_path, output_path)

    @staticmethod
    def convert_file(input_path: str, output_path: str):
        try:
            audio = AudioSegment.from_file(input_path, format="mp4")
            audio.export(output_path, format="mp3")
        except Exception as e:
            print(f"שגיאה בהמרת {input_path}: {e}")
