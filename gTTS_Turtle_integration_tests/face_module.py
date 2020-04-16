import turtle

def eye_draw(eye, eye_color, eye_fill):
    # Define the eye color
    eye.color(eye_color)

    # Eye
    eye.begin_fill()
    for i in range(3):
        eye.forward(100)
        eye.left(90)

    eye.forward(100)
    if (eye_fill == True):
        eye.end_fill()

def mouth_draw(mouth, mouth_color, mouth_fill):
    # Define the mouth color
    mouth.color(mouth_color)
    # Mouth
    mouth.begin_fill()
    mouth.left(45)
    mouth.forward(100)
    mouth.left(45)
    mouth.forward(160)
    mouth.left(45)
    mouth.forward(100)
    mouth.left(135)
    mouth.forward(300)
    if (mouth_fill == True):
        mouth.end_fill()

def pen_move(face_element, x, y, left, right):
    face_element.penup()

    # Coordinates
    face_element.setx(x)
    face_element.sety(y)

    # Angles
    face_element.left(left)
    face_element.right(right)   
    face_element.pendown()

def face_draw(first_run, is_speaking):
    right_eye = turtle.Turtle()
    left_eye = turtle.Turtle()
    mouth = turtle.Turtle()
    turtle.bgcolor("black")

    if (first_run == True):
        eye_draw(right_eye, "cyan", True)
        pen_move(left_eye, -150, 0, 0, 0)
        eye_draw(left_eye, "cyan", True)

    if (is_speaking == True):
        pen_move(mouth, -180, -50, 0, 90)
        mouth_draw(mouth, "cyan", True)
        
    else:
        pen_move(mouth, -180, -50, 0, 90)
        mouth_draw(mouth, "black", True)
        




        