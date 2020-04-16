import speak_module
import face_module

def main():
    first_run = True
    text = "Olá, meu nome é ROSA, como posso ajudá-lo?"

    while(True): 
        if (text != ""):
            is_speaking = True
        else:
            is_speaking = False
        
        face_module.face_draw(first_run, is_speaking)
        speak_module.speak(text)

        first_run = False
        text = ""

main()