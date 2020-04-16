from gtts import gTTS
import os
import playsound  as ps

def speak(text):
    if (text == ""):
        pass

    else:
        tts = gTTS(text=text, lang="pt")
        filename = "voice.mp3"
        tts.save(filename)
        ps.playsound(filename)
        os.remove("voice.mp3")

def conversation(text, text_part, answer):
    if text_part in text:
        speak(answer)

