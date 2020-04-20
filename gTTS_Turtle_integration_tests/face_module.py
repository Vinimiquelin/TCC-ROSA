import turtle

def talloval(turtle, r):               # Verticle Oval
    turtle.left(45)
    for loop in range(2):      # Draws 2 halves of ellipse
        turtle.circle(r,90)    # Long curved part
        turtle.circle(r/2,90)  # Short curved part

def flatoval(turtle, r):               # Horizontal Oval
    turtle.right(45)
    for loop in range(2):
        turtle.circle(r,90)
        turtle.circle(r/2,90)


def eye_draw(eye, eye_color, eye_shape, eye_fill):
    # Define the eye color
    eye.color(eye_color)

    if (eye_shape == "square"):
        # Square eye
        eye.begin_fill()
        for i in range(3):
            eye.forward(100)
            eye.left(90)

        eye.forward(100)

        if (eye_fill == True):
            eye.end_fill()
    
    elif (eye_shape == "circle"):
        # Circle eye
        eye.begin_fill()
        eye.circle(50)

        if (eye_fill == True):
            eye.end_fill()

    elif (eye_shape == "ellipse"):
        #Ellipse eye
        eye.begin_fill()
        talloval(eye, 80)

        if (eye_fill == True):
            eye.end_fill()

    else:
        raise Exception("Não existe o formato "+eye_shape+" para os olhos!")

def mouth_draw(mouth, mouth_color, mouth_shape, mouth_fill):
    # Define the mouth color
    mouth.color(mouth_color)
    if (mouth_shape == "trapeze"):
        # Trapeze mouth
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

    elif (mouth_shape == "circle"):
        # Circle mouth
        mouth.begin_fill()
        mouth.circle(20)
        if (mouth_fill == True):
            mouth.end_fill()

    elif (mouth_shape == "ellipse"):
        #Ellipse eye
        mouth.begin_fill()
        talloval(mouth, 30)

        if (mouth_fill == True):
            mouth.end_fill()

    else:
        raise Exception("Não existe o formato "+mouth_shape+" para a boca!")
    

def pen_move(face_element, x, y, left, right):
    face_element.penup()

    # Coordinates
    face_element.setx(x)
    face_element.sety(y)

    # Angles
    face_element.left(left)
    face_element.right(right)   
    face_element.pendown()

def face_draw(first_run, is_speaking, face_color, bg_color, face_shape, is_filled):
    right_eye = turtle.Turtle()
    left_eye = turtle.Turtle()
    mouth = turtle.Turtle()
    turtle.bgcolor(bg_color)

    if (first_run == True):
        pen_move(right_eye, 100, 0, 0, 0)
        eye_draw(right_eye, face_color, face_shape, is_filled)
        pen_move(left_eye, -80, 0, 0, 0)
        eye_draw(left_eye, face_color, face_shape, is_filled)

    if (is_speaking == True):
        pen_move(mouth, -40, -80, 0, 90)
        mouth_draw(mouth, face_color, face_shape, is_filled)
        
    else:
        pen_move(mouth, -40, -80, 0, 90)
        mouth_draw(mouth, bg_color, face_shape, is_filled)
        




        