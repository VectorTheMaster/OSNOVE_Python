import turtle
import random

boje = ["blue", "yellow", "black", "pink",
        "brown", "red", "purple", "gray", "green"]

a = turtle.Turtle()
a.speed(0)
a.pensize(2)


def up():
    a.setheading(90)
    a.fd(100)


def down():
    a.setheading(270)
    a.fd(100)


def left():
    a.setheading(180)
    a.fd(100)


def right():
    a.setheading(0)
    a.fd(100)


def clickleft(x, y):
    a.color(random.choice(boje))


def clickright(x, y):
    a.stamp()  # crta strelicu


turtle.listen()  # pokrećemo events

turtle.onscreenclick(clickleft, 1)
turtle.onscreenclick(clickright, 3)


turtle.onkey(up, "w")
turtle.onkey(left, "a")
turtle.onkey(down, "s")
turtle.onkey(right, "d")


turtle.mainloop()


turtle.done()
