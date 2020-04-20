import speak_module
import face_module
import listen_module

def main():
    face_color = "magenta"
    eyes_color = "turquoise"
    mouth_color = "pink"
    bg_color = "black"
    face_shape = "circle"
    eyes_shape = "ellipse"
    mouth_shape = "ellipse"
    face_is_filled = True
    eyes_is_filled = True
    mouth_is_filled = False
    trigger_words = speak_module.trigger_words_function()
    answers = speak_module.answers_function()
    face_module.full_face_draw(face_color, eyes_color, mouth_color, bg_color, face_shape, eyes_shape, mouth_shape, face_is_filled, eyes_is_filled, mouth_is_filled)

    while(True):
        text = listen_module.get_audio()
        if "Rosa" in text:
            cont = 0
            face_module.speak_feedback(eyes_color, face_color,face_shape)
            speak_module.speak("Estou te ouvindo")
            text = listen_module.get_audio()
            face_module.speak_feedback(eyes_color, face_color, face_shape)
            for x in range(len(trigger_words)):
                understood = speak_module.conversation(text, trigger_words[x], answers[x])
                if (understood == True):
                    cont += 1

            if (cont == 0):
                speak_module.speak("Desculpe... não entendi o que você disse.")   
           
        if "durma" in text:
            face_module.speak_feedback(eyes_color, face_color, face_shape)
            speak_module.speak("Desligando todos os sistemas. Até mais!")
            break

main()