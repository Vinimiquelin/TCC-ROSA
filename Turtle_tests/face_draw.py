import turtle

face = turtle.Turtle()
face.color("cyan")
turtle.bgcolor("black")

# Right eye
face.begin_fill()
for i in range(3):
    face.forward(100)
    face.left(90)

face.forward(100)
face.end_fill()

# Moving the pen
face.penup()
for i in range(2):
    face.left(90)
    face.forward(100)

face.left(90)
face.forward(200)
face.pendown()

# Left eye
face.begin_fill()
for i in range(3):
    face.forward(100)
    face.left(90)

face.forward(100)
face.end_fill()

# Moving the pen
face.penup()
face.left(90)
face.forward(100)
face.left(90)
face.forward(200)
face.pendown()

# Mouth
face.begin_fill()
face.left(45)
face.forward(100)
face.left(45)
face.forward(160)
face.left(45)
face.forward(100)
face.left(135)
face.forward(300)
face.end_fill()
turtle.done()
