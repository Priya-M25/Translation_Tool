pip install googletrans==4.0.0-rc1

import nltk
from googletrans import Translator
def translate_text(text, src_lang, dest_lang):
    translator = Translator()
    translation = translator.translate(text, src=src_lang, dest=dest_lang)
    translated_text = translation.text
    return translated_text
def french_to_english(french_text):
    french_tokens = nltk.word_tokenize(french_text)
    french_text_cleaned = ' '.join(french_tokens)
    english_translation = translate_text(french_text_cleaned, 'fr', 'en')
    return english_translation
def english_to_french(english_text):
    french_translation = translate_text(english_text, 'en', 'fr')
    return french_translation
if __name__ == "__main__":
    while True:
        choice = input("Enter '1' for French to English translation, '2' for English to French translation, or 'q' to quit: ")
        if choice == '1':
            french_text = input("Enter French text to translate into English: ")
            english_translation = french_to_english(french_text)
            print("Translated English text:", english_translation)
        elif choice == '2':
            english_text = input("Enter English text to translate into French: ")
            french_translation = english_to_french(english_text)
            print("Translated French text:", french_translation)
        elif choice.lower() == 'q':
            print("Quitting...")
            break
        else:
            print("Invalid choice. Please enter '1', '2', or 'q'.")


