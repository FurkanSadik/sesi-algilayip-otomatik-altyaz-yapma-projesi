import srt
from datetime import timedelta
from translate_text import translate_text

def save_srt(segments, output_srt_path="output.srt", translate=False):
    """Segmentleri SRT formatinda kaydeder."""
    subtitles = []
    for i, segment in enumerate(segments):
        start = timedelta(seconds=segment["start"])
        end = timedelta(seconds=segment["end"])
        text = segment["text"]
        
        if translate:
            text = translate_text(text, "en")  # İngilizce çeviri yap
        
        subtitles.append(srt.Subtitle(index=i+1, start=start, end=end, content=text))
    
    with open(output_srt_path, "w", encoding="utf-8") as f:
        f.write(srt.compose(subtitles))
    
    return output_srt_path
