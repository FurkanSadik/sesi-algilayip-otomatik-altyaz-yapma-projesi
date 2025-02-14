import os
from gui import select_video, get_language_choice
from extract_audio import extract_audio
from transcribe_audio import transcribe_audio
from save_srt import save_srt

def main():
    video_path = select_video()
    if not video_path:
        print("❌ Video seçilmedi, çikiliyor...")
        return

    language = get_language_choice()
    
    audio_path = "temp_audio.wav"
    srt_path = "output.srt"

    print("📤 Videodan ses çikartiliyor...")
    extract_audio(video_path, audio_path)

    print("🎙 Konuşmalar analiz ediliyor...")
    segments = transcribe_audio(audio_path, language="tr")

    print(f"📄 '{language}' dilinde altyazi oluşturuluyor...")
    srt_file = save_srt(segments, srt_path, translate=(language == "en"))

    print(f"✅ Altyazi dosyasi oluşturuldu: {srt_file}")

    # Geçici dosyayı temizle
    if os.path.exists(audio_path):
        os.remove(audio_path)

if __name__ == "__main__":
    main()
