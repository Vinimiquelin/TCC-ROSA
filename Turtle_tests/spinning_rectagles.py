import turtle

turtle.speed(0)
turtle.bgcolor("black")

for i in range(5):
    for colours in ["red", "magenta", "blue", "cyan", "green", "yellow", "white"]:
        turtle.color(colours)
        turtle.pensize(3)
        turtle.left(12)
        for j in range(4):
            turtle.forward(200)
            turtle.left(90)