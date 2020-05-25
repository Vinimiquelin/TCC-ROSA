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

'''
def conversation(text, trigger_word, answer):
    understood = False
    if trigger_word in text:
        speak(answer)
        understood = True


    return understood
'''

def trigger_words_function():
    trigger_words = [
        "como vai você", 
        "Por que seu nome é Rosa", 
        "Como eu chego na sala a três",
        "sim"]

    return trigger_words

def answers_function():
    answers = [
        "Vou bem, melhor agora que você chegou!", 
        "O nome ROSA significa robô sociável assistivo de apoio. Estou aqui para te ajudar no que você precisar", 
        "Você vai precisar virar a esquerda e depois à direita. Quer que eu te acompanhe?",
        "Então vamos lá!"]

    return answers

