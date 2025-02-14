import whisper

def transcribe_audio(audio_path, language="tr"):
    """Ses dosyasini metne çevirir."""
    model = whisper.load_model("base")  # Daha hızlı olması için "tiny" da seçilebilir
    result = model.transcribe(audio_path, language=language)
    return result["segments"]  # Zaman damgalı metni döndürür
