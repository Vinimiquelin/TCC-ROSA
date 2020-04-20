import speak_module
import face_module
import listen_module

def main():
    first_run = True
    is_speaking = False
    face_color = "pink"
    bg_color = "black"
    face_shape = "ellipse"
    is_filled = True
    trigger_words = speak_module.trigger_words_function()
    answers = speak_module.answers_function()

    while(True):
        text = listen_module.get_audio()

        if (first_run == True):
            face_module.face_draw(first_run, is_speaking, face_color, bg_color, face_shape, is_filled)
            first_run = False

        if "Rosa" in text:
            is_speaking = True
            face_module.face_draw(first_run, is_speaking, face_color, bg_color, face_shape, is_filled)
            speak_module.speak("Estou te ouvindo")

            while(True):
                text = listen_module.get_audio()
                face_module.face_draw(first_run, is_speaking, face_color, bg_color, face_shape, is_filled)
                for x in range(len(trigger_words)):
                    speak_module.conversation(text, trigger_words[x], answers[x])

                if (text == ""):
                    speak_module.speak("Me chame se precisar de algo")
                    is_speaking = False
                    face_module.face_draw(first_run, is_speaking, face_color, bg_color, face_shape, is_filled)
                    break
           
        if "durma" in text:
            is_speaking = True
            face_module.face_draw(first_run, is_speaking, face_color, bg_color, face_shape, is_filled)
            speak_module.speak("Desligando todos os sistemas. Até mais!")
            break

main()