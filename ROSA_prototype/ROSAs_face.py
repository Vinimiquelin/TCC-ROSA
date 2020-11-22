from ROSA_modules import face_module

# ROSA's face
face_color = "magenta"
eyes_color = "pink"
mouth_color = "magenta"
feedback_color = "pink"
text_color = "pink"
bg_color = "black"
face_shape = "circle"
eyes_shape = "mad"
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

while(True):
    pass