from ROSA_modules import speak_module
from ROSA_modules import face_module
from ROSA_modules import listen_module
from ROSA_modules import recognize_module

def main():
    # ROSA's questions and answers
    turn_on_phrase = "Sistema iniciado... Olá, meu nome é Rosa! Se precisar de mim, chame pelo meu nome."
    trigger_words = speak_module.trigger_words_function()
    answers = speak_module.answers_function()
    turn_off_phrase = "Desligando todos os sistemas. Até mais!"
    understood_phrase = "Estou te ouvindo "
    misunderstood_phrase = "Desculpe... não entendi o que você disse "

    # ROSA's face
    face_color = "magenta"
    eyes_color = "pink"
    mouth_color = "magenta"
    feedback_color = "pink"
    text_color = "pink"
    bg_color = "black"
    face_shape = "circle"
    eyes_shape = "ellipse"
    mouth_shape = "ellipse"
    feedback_shape = "circle_text"
    face_size = 400
    eyes_size = 150
    mouth_size = 50
    face_is_filled = True
    eyes_is_filled = True
    mouth_is_filled = True
    face_fill_color = "pink"
    eyes_fill_color = "magenta"
    mouth_fill_color = "pink"
    text_fill_color = "magenta"
    has_face = False
    has_eyes = True
    has_mouth = False

    screen = face_module.screen_setup()
    face, right_eye, left_eye, mouth, feedback, bg, turtle_text = face_module.create_turtles()
    face_module.full_face_draw(screen, face, right_eye, left_eye, mouth, bg, face_color, eyes_color, mouth_color, bg_color, face_shape, eyes_shape, mouth_shape, face_size, eyes_size, mouth_size, face_is_filled, eyes_is_filled, mouth_is_filled, face_fill_color, eyes_fill_color, mouth_fill_color, has_face, has_eyes, has_mouth)
    
    # ROSA's face recognition
    faceCascade, clf, video_capture = recognize_module.face_detection_preset()

    # Welcome phrase
    face_module.speak_feedback(feedback, feedback_color, bg_color,feedback_shape)
    face_module.write_text(turn_on_phrase, turtle_text, text_color, text_fill_color, 24, -700, -400)
    speak_module.speak(turn_on_phrase)
    face_module.reset_turtle(turtle_text)

    while(True):
        img = recognize_module.video_read(video_capture)
        username = recognize_module.recognize(img, clf, faceCascade, 1.1, 10)
        text = listen_module.get_audio()
        if "Rosa" in text:
            # Happy eyes if someone talks with ROSA
            eyes_shape = "happy"
            face_module.reset_turtle(right_eye)
            face_module.reset_turtle(left_eye)
            face_module.full_face_draw(screen, face, right_eye, left_eye, mouth, bg, face_color, eyes_color, mouth_color, bg_color, face_shape, eyes_shape, mouth_shape, face_size, eyes_size, mouth_size, face_is_filled, eyes_is_filled, mouth_is_filled, face_fill_color, eyes_fill_color, mouth_fill_color, has_face, has_eyes, has_mouth)

            understood = False
            face_module.speak_feedback(feedback, feedback_color, feedback_color,feedback_shape)
            face_module.write_text(understood_phrase+username, turtle_text, text_color, text_fill_color, 24, -700, -400)
            speak_module.speak(understood_phrase+username)
            face_module.reset_turtle(turtle_text)

            text = listen_module.get_audio()
            for x in range(len(trigger_words)):
                if trigger_words[x] in text:
                    face_module.speak_feedback(feedback, feedback_color, feedback_color,feedback_shape)
                    face_module.write_text(answers[x], turtle_text, text_color, text_fill_color, 24, -700, -400)
                    speak_module.speak(answers[x])
                    face_module.reset_turtle(turtle_text)
                    understood = True

            if (understood == False):
                # Sad eyes when ROSA misunderstoods
                eyes_shape = "sad"
                face_module.reset_turtle(right_eye)
                face_module.reset_turtle(left_eye)
                face_module.full_face_draw(screen, face, right_eye, left_eye, mouth, bg, face_color, eyes_color, mouth_color, bg_color, face_shape, eyes_shape, mouth_shape, face_size, eyes_size, mouth_size, face_is_filled, eyes_is_filled, mouth_is_filled, face_fill_color, eyes_fill_color, mouth_fill_color, has_face, has_eyes, has_mouth)

                face_module.speak_feedback(feedback, feedback_color, feedback_color,feedback_shape)
                face_module.write_text(misunderstood_phrase+username, turtle_text, text_color, text_fill_color, 24, -700, -400)
                speak_module.speak(misunderstood_phrase+username)
                face_module.reset_turtle(turtle_text)

            # Neutral eyes when the conversation ends
            eyes_shape = "ellipse"
            face_module.reset_turtle(right_eye)
            face_module.reset_turtle(left_eye)
            face_module.full_face_draw(screen, face, right_eye, left_eye, mouth, bg, face_color, eyes_color, mouth_color, bg_color, face_shape, eyes_shape, mouth_shape, face_size, eyes_size, mouth_size, face_is_filled, eyes_is_filled, mouth_is_filled, face_fill_color, eyes_fill_color, mouth_fill_color, has_face, has_eyes, has_mouth)

                          
        if "durma" in text:
            face_module.speak_feedback(feedback, feedback_color, feedback_color,feedback_shape)
            # Good bye phrase
            face_module.write_text(turn_off_phrase, turtle_text, text_color, text_fill_color, 24, -700, -400)
            speak_module.speak(turn_off_phrase)
            face_module.reset_turtle(turtle_text)

            # releasing web-cam
            recognize_module.video_release(video_capture)
            break

main()