import turtle
import random

def talloval(turtle, r):               # Verticle Oval
    turtle.left(45)
    for loop in range(2):      # Draws 2 halves of ellipse
        turtle.circle(r,90)    # Long curved part
        turtle.circle(r/2,90)  # Short curved part
    turtle.right(45)

def flatoval(turtle, r):               # Horizontal Oval
    turtle.right(45)
    for loop in range(2):
        turtle.circle(r,90)
        turtle.circle(r/2,90)
    turtle.right(45)
    

def face_draw(face, face_color, face_shape, face_size, face_fill, face_fill_color):
    # Face settings
    face.hideturtle() # Hide the cursor
    face.speed(10) # Setting turtles speed
    face.width(10) # Setting the width of the pen
    face.color(face_color) # Define the color

    if (face_shape == "circle"):
        # Circle face  
        pen_move(face, 0, -400, 0)
        face.begin_fill()
        face.circle(face_size)

        if (face_fill == True):
            face.color(face_fill_color)
            face.end_fill()

    else:
        raise Exception("Não existe o formato "+face_shape+" para a face!")

def speak_feedback(feedback, feedback_color, pen_color, feedback_shape):
    feedback.hideturtle() # Hide the cursor
    feedback.speed(10) # Setting turtles speed
    feedback.width(20) # Setting the width of the pen 
    feedback.color(feedback_color) # Define the color

    if (feedback_shape == "circle_face"):
        # Circle face feedback
        pen_move(feedback, 0, -400, 0)
        feedback.begin_fill()
        feedback.circle(400)
        feedback.color(pen_color)
        feedback.reset()

    elif (feedback_shape == "ellipse_mouth"):
        # Ellipse mouth feedback
        pen_move(feedback, 0, -200, 0)
        feedback.begin_fill()
        flatoval(feedback, 30)
        feedback.color(pen_color)
        feedback.reset()

    elif (feedback_shape == "circle_text"):
        # Ellipse mouth feedback
        pen_move(feedback, 0, -400, 0)
        feedback.begin_fill()
        feedback.circle(50)
        feedback.color(pen_color)
        feedback.reset()

    else:
        raise Exception("Não existe o formato "+feedback_shape+" para o feedback de fala!")


def eye_draw(eye, eye_color, eye_shape, eye_size, eye_fill, eye_fill_color, eye_side):
    # Eye settings
    eye.hideturtle() # Hide the cursor
    eye.speed(10) # Setting turtles speed
    eye.width(10) # Setting the width of the pen
    eye.color(eye_color) # Define the color

    if (eye_shape == "square"):
        # Square eye
        if (eye_side == "right"):
            pen_move(eye, 200, -100, 0)
            eye.begin_fill()
            for i in range(3):
                eye.forward(eye_size)
                eye.left(90)

            eye.forward(eye_size)

            if (eye_fill == True):
                eye.color(eye_fill_color)
                eye.end_fill()

        if (eye_side == "left"):
            pen_move(eye, -250, -100, 0)
            eye.begin_fill()
            for i in range(3):
                eye.forward(eye_size)
                eye.left(90)

            eye.forward(eye_size)

            if (eye_fill == True):
                eye.color(eye_fill_color)
                eye.end_fill()
    
    elif (eye_shape == "circle"):
        # Circle eye
        if (eye_side == "right"):
            pen_move(eye, 200, -100, 0)
            eye.begin_fill()
            eye.circle(eye_size)

            if (eye_fill == True):
                eye.color(eye_fill_color)
                eye.end_fill()

        if (eye_side == "left"):
            pen_move(eye, -250, -100, 0)
            eye.begin_fill()
            eye.circle(eye_size)

            if (eye_fill == True):
                eye.color(eye_fill_color)
                eye.end_fill()

    elif (eye_shape == "ellipse"):
        #Ellipse eye
        if (eye_side == "right"):
            pen_move(eye, 300, -100, 0)
            eye.begin_fill()
            talloval(eye, eye_size)

            if (eye_fill == True):
                eye.color(eye_fill_color)
                eye.end_fill()
        
        if (eye_side == "left"):
            pen_move(eye, -150, -100, 0)
            eye.begin_fill()
            talloval(eye, eye_size)

            if (eye_fill == True):
                eye.color(eye_fill_color)
                eye.end_fill()
  
    elif (eye_shape == "happy"):
        #Happy eye
        if (eye_side == "right"):
            pen_move(eye, 400, -100, 0)
            eye.width(50)
            eye.left(90)
            eye.begin_fill()
            eye.circle(eye_size, 180)
            eye.right(90)

        if (eye_side == "left"):
            pen_move(eye, -50, -100, 0)
            eye.width(50)
            eye.left(90)
            eye.begin_fill()
            eye.circle(eye_size, 180)
            eye.right(90)

    elif (eye_shape == "sad"):
        #Sad eye
        if (eye_side == "right"):
            pen_move(eye, 100, 0, 0)
            eye.left(-90)
            eye.begin_fill()
            eye.circle(eye_size, 160)
            eye.right(-90)

        if (eye_side == "left"):
            pen_move(eye, -100, 0, 0)
            eye.left(-270)
            eye.begin_fill()
            eye.circle(eye_size, -160)
            eye.right(-270)

        if (eye_fill == True):
            eye.color(eye_fill_color)
            eye.end_fill()

    elif (eye_shape == "mad"):
        #Mad eye
        if (eye_side == "right"):
            pen_move(eye, 100, 0, 0)
            eye.left(-90)
            eye.begin_fill()
            eye.circle(eye_size, 220)
            eye.right(-90)
  
        if (eye_side == "left"):
            pen_move(eye, -100, 0, 0)
            eye.left(-270)
            eye.begin_fill()
            eye.circle(eye_size, -220)
            eye.right(-270)

        if (eye_fill == True):
            eye.color(eye_fill_color)
            eye.end_fill()

    else:
        raise Exception("Não existe o formato "+eye_shape+" para os olhos!")

def mouth_draw(mouth, mouth_color, mouth_shape, mouth_size, mouth_fill, mouth_fill_color):
    # Mouth settings
    mouth.hideturtle() # Hide the cursor
    mouth.speed(10) # Setting turtles speed
    mouth.width(10) # Setting the width of the pen
    mouth.color(mouth_color)  # Define the color

    if (mouth_shape == "happy"):
        # Trapeze mouth
        pen_move(mouth, -120, -200, -90)
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
            mouth.color(mouth_fill_color)
            mouth.end_fill()

    elif (mouth_shape == "circle"):
        # Circle mouth
        pen_move(mouth, 0, -200, 0)
        mouth.begin_fill()
        mouth.circle(mouth_size)
        if (mouth_fill == True):
            mouth.color(mouth_fill_color)
            mouth.end_fill()

    elif (mouth_shape == "ellipse"):
        #Ellipse mouth
        pen_move(mouth, 0, -200, 0)
        mouth.begin_fill()
        flatoval(mouth, mouth_size)

        if (mouth_fill == True):
            mouth.color(mouth_fill_color)
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

def screen_setup():
    # Screen setup
    screen = turtle.Screen()
    screen.setup(width = 1.0, height = 1.0)

    # Remove close, minimaze and maximaze buttons:
    canvas = screen.getcanvas()
    root = canvas.winfo_toplevel()
    root.overrideredirect(1)

    return screen

def create_turtles():
    # Creating the turtles
    face = turtle.Turtle()
    right_eye = turtle.Turtle()
    left_eye = turtle.Turtle()
    mouth = turtle.Turtle()
    feedback = turtle.Turtle()
    bg = turtle.Turtle()
    text = turtle.Turtle()

    return face, right_eye, left_eye, mouth, feedback, bg, text

def full_face_draw(screen, face, right_eye, left_eye, mouth, bg, face_color, eyes_color, mouth_color, bg_color, face_shape, eyes_shape, mouth_shape, face_size, eyes_size, mouth_size, face_is_filled, eyes_is_filled, mouth_is_filled, face_fill_color, eyes_fill_color, mouth_fill_color, has_face, has_eyes, has_mouth):  
    # Add background color
    turtle.bgcolor(bg_color)

    if (has_face == True):
        face_draw(face, face_color, face_shape, face_size, face_is_filled, face_fill_color)

    if (has_eyes == True):
        eye_draw(right_eye, eyes_color, eyes_shape, eyes_size, eyes_is_filled, eyes_fill_color, "right")
        eye_draw(left_eye, eyes_color, eyes_shape, eyes_size, eyes_is_filled, eyes_fill_color, "left")

    if (has_mouth == True):
        mouth_draw(mouth, mouth_color, mouth_shape, mouth_size, mouth_is_filled, mouth_fill_color)
           
def write_text(text, turtle_text, font_color, text_fill_color, font_size, x, y):
    turtle_text.hideturtle() # Hide the cursor
    turtle_text.speed(10) # Setting turtles speed
    turtle_text.width(10) # Setting the width of the pen
    turtle_text.color(font_color) # Define the color

    # Text rectangle
    pen_move(turtle_text, x-20, y, 0)
    turtle_text.begin_fill()
        
    turtle_text.forward(1400)
    turtle_text.left(90)
    turtle_text.forward(100)
    turtle_text.left(90)
    turtle_text.forward(1400)
    turtle_text.left(90)
    turtle_text.forward(100)

    turtle_text.color(text_fill_color)
    turtle_text.end_fill()

    # Write text
    turtle_text.color(font_color)
    pen_move(turtle_text, x, y, 0)
    turtle_text.write(text, font=("Arial", font_size, "bold"))

def reset_turtle(turtle):
    turtle.reset()



        