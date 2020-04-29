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

def face_draw(face, face_color, face_shape, face_fill):
    # Define the face color
    face.color(face_color)

    if (face_shape == "circle"):
        # Circle face
        face.begin_fill()
        face.circle(200)

        if (face_fill == True):
            face.end_fill()

    else:
        raise Exception("Não existe o formato "+face_shape+" para a face!")

def speak_feedback(feedback_color, pen_color, feedback_shape):
    # Creating feedback turtle
    feedback = turtle.Turtle()

    # Setting the width of the pen
    feedback.width(20)

    # Define the feedback color
    feedback.color(feedback_color)

    if (feedback_shape == "circle"):
        # Circle feedback
        pen_move(feedback, -20, -150, 0)
        feedback.begin_fill()
        feedback.circle(200)
        feedback.clear()
        feedback.color(pen_color)


    elif (feedback_shape == "ellipse"):
        #Ellipse feedback
        pen_move(feedback, -40, -80, 0)
        feedback.begin_fill()
        flatoval(feedback, 30)
        feedback.clear()

    else:
        raise Exception("Não existe o formato "+feedback_shape+" para o feedback de fala!")


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
        #Ellipse mouth
        mouth.begin_fill()
        flatoval(mouth, 30)

        if (mouth_fill == True):
            mouth.end_fill()

    else:
        raise Exception("Não existe o formato "+mouth_shape+" para a boca!")
    

def pen_move(face_element, x, y, angle):
    face_element.penup()

    # Coordinates
    face_element.setx(x)
    face_element.sety(y)

    # Angles
    face_element.left(angle) 
    face_element.pendown()

def full_face_draw(face_color, eyes_color, mouth_color, bg_color, face_shape, eyes_shape, mouth_shape, face_is_filled, eyes_is_filled, mouth_is_filled):
    # Screen setup
    screen = turtle.Screen()
    screen.setup(width = 1.0, height = 1.0)

    # Remove close, minimaze and maximaze buttons:
    canvas = screen.getcanvas()
    root = canvas.winfo_toplevel()
    root.overrideredirect(1)

    # Creating the turtles
    face = turtle.Turtle()
    right_eye = turtle.Turtle()
    left_eye = turtle.Turtle()
    mouth = turtle.Turtle()
    turtle.bgcolor(bg_color)

    # Setting the width of the pen
    face.width(10)
    right_eye.width(10)
    left_eye.width(10)
    mouth.width(10)

    pen_move(face, -20, -150, 0)
    face_draw(face, face_color, face_shape, face_is_filled)
    pen_move(right_eye, 100, 0, 0)
    eye_draw(right_eye, eyes_color, eyes_shape, eyes_is_filled)
    pen_move(left_eye, -80, 0, 0)
    eye_draw(left_eye, eyes_color, eyes_shape, eyes_is_filled)
    pen_move(mouth, -40, -80, 0)
    mouth_draw(mouth, mouth_color, mouth_shape, mouth_is_filled)

        
        




        