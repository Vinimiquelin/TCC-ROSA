from ROSA_modules import speak_module
from ROSA_modules import face_module
from ROSA_modules import listen_module
from ROSA_modules import recognize_module

def main():
    # ROSA's questions and answers
    trigger_words = speak_module.trigger_words_function()
    answers = speak_module.answers_function()

    # ROSA's face
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
    face_module.full_face_draw(face_color, eyes_color, mouth_color, bg_color, face_shape, eyes_shape, mouth_shape, face_is_filled, eyes_is_filled, mouth_is_filled)
    
    # ROSA's face recognition
    faceCascade, clf, video_capture = recognize_module.face_detection_preset()

    # Welcome phrase
    face_module.speak_feedback(eyes_color, face_color,face_shape)
    speak_module.speak("Iniciaanndo sistema... Olá, meu nome é Rosa! Se precisar de mim, chame pelo meu nome.")

    while(True):
        img = recognize_module.video_read(video_capture)
        username = recognize_module.recognize(img, clf, faceCascade, 1.1, 10)
        text = listen_module.get_audio()
        if "Rosa" in text:
            understood = False
            face_module.speak_feedback(eyes_color, face_color,face_shape)
            speak_module.speak("Estou te ouvindo "+username)
            text = listen_module.get_audio()
            face_module.speak_feedback(eyes_color, face_color, face_shape)
            for x in range(len(trigger_words)):
                understanding = speak_module.conversation(text, trigger_words[x], answers[x])
                if (understanding == True):
                    understood = True

            if (understood == False):
                speak_module.speak("Desculpe... não entendi o que você disse.")   
           
        if "durma" in text:
            face_module.speak_feedback(eyes_color, face_color, face_shape)
            # Good bye phrase
            speak_module.speak("Desligando todos os sistemas. Até mais!")
            # releasing web-cam
            recognize_module.video_release(video_capture)
            break

main()