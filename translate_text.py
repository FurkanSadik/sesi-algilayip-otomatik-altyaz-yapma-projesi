from deep_translator import GoogleTranslator

def translate_text(text, target_lang="en"):
    """Metni belirtilen dile çevirir."""
    translator = GoogleTranslator(source="auto", target=target_lang)
    return translator.translate(text)
