from deep_translator import MyMemoryTranslator

" This file contains functions for translating between english and french "

def english_to_french(english_text):
    """translates english to french"""
    french_text = MyMemoryTranslator(source='en', target='fr').translate(text=english_text)
    return french_text

def french_to_english(french_text):
    """translates french to english"""
    english_text = MyMemoryTranslator(source='fr', target='en').translate(text=french_text)
    return english_text
