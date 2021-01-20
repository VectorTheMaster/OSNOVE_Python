import turtle

s = turtle.Screen()
a = turtle.Turtle()
a.speed(-1)


def dragging(x, y):
    a.ondrag(None)
    a.setheading(a.towards(x, y))
    a.goto(x, y)
    a.ondrag(dragging)


def clickright(x,y):
    a.clear()


def main():
    turtle.listen()

    a.ondrag(dragging)

    turtle.onscreenclick(clickright, 3)

    s.mainloop()


main()

turtle.done()
