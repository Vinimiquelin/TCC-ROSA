import speech_recognition as sr

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

