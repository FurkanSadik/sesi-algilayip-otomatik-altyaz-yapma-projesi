import subprocess

def extract_audio(video_path, output_audio_path="temp_audio.wav"):
    """Videodan sesi çikarir ve belirtilen dosyaya kaydeder."""
    command = ["ffmpeg", "-i", video_path, "-q:a", "0", "-map", "a", output_audio_path, "-y"]
    subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return output_audio_path
