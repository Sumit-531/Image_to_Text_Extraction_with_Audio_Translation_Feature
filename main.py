from gtts import gTTS
import pytesseract
import PIL.Image
from googletrans import Translator
import os


# Text extraction from Image(OCR=Optical Character Recognition)
# psm = Page segmentation mode, oem = OCR engine mode
language = "eng"
myconfig = f"--psm 6 --oem 3 -l {language}"

text = pytesseract.image_to_string(PIL.Image.open("Quotes.jpg"), config=myconfig)
print(text)

# USER CHOICE
user_input = input("Which language do you want to translate?: ").lower()
languages = {
    "bengali": "bn",
    "english": "en",
    "tamil": "ta",
    "telugu": "te",
    "japanese": "ja",
    "german": "de",
}
if user_input in languages:
    lang = languages[user_input]
else:
    lang = "en"

# Translation(GoogleTrans)
translator = Translator()
translated_text = translator.translate(text=text, dest=lang)
text2 = translated_text.text

# Text to speech(gtts=Google Text to Speech)
# gtts language
language = lang

output_speech = gTTS(text=text2, lang=language, slow=False)
output_speech.save("audio.mp3")

os.system("start audio.mp3")
