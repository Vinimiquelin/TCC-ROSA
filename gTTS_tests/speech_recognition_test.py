from gtts import gTTS
import os
import playsound  as ps
import speech_recognition as sr

def speak(text):
    tts = gTTS(text=text, lang="pt")
    filename = "voice.mp3"
    tts.save(filename)
    ps.playsound(filename)
    os.remove("voice.mp3")

def get_audio():
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio, language="pt-PT")
            print(said)
        except Exception as e:
            print("Exception: "+str(e))

    return said

def conversation(text, text_part, answer):
    if text_part in text:
        speak(answer)

while(True):
    text = get_audio()

    if "acorde" in text:
        speak("Todos os sistemas em operação. Agora estou te ouvindo")
        while(True):
            trigger_words = [
            "Olá", 
            "vou bem", 
            "Qual é o seu nome",
            "obrigado"]

            answers = [
            "Olá, como vai você?", 
            "Que bom, eu também", 
            "Meu nome é ROSA, robô sociável assistivo. Estou aqui para te ajudar no que você precisar",
            "O prazer é todo meu"]

            text = get_audio()

            for x in range(len(trigger_words)):
                conversation(text, trigger_words[x], answers[x])

            if "durma" in text:
                speak("Ativando o modo de repouso")
                break
            
    
    if "desligar" in text:
        speak("Desligando todos os sistemas, até mais")
        break



