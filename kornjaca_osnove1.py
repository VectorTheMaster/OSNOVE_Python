import turtle  # VAZNO kako bismo imali kornjacu
import random

boje = ["blue", "yellow", "black", "pink",
        "brown", "red", "purple", "gray", "green"]


s = turtle.Screen()  # definirali smo s kao screen gdje cemo crtati
a = turtle.Turtle()  # varijablu a definiramo kao kornjacu, MOZE SE DEFINIRATI I VISE KORNJACA PA SE MOZE CRTATI S VISE NJIH U ISTO VRIJEME
a.speed(0)  # brzina kretanja kornjače, ako se stavi 0 nacrta se automatski
a.pensize(5)  # definirali smo debljinu crte
# definirali smo boju kornjace, moze i ostale boje, druga boja je ona koju koristimo u fill opcijama
a.color("black", "yellow")
# oznacava nam da ce se kornjaca u pocetku okrenuti 90 stupnjeva u lijevo, inace gleda prema desno
a.setheading(90)

#   a.fd(100) ili a.forward(100)  kornjaca ide naprijed za 100
#   a.bk(100)  ili a.backward(100)  kornjaca ide u nazad za 100
#   a.lt(90)  ili a.left(90)  okrece kornjacu za 90 stupnjeva u lijevo
#   a.rt(90)    ili a.right(90) okrece kornjacu za 90 stupnjeva u desno
#   a.penup() kornjaca se podigne i ne ostavlja trag
#   a.pendown() kornjaca se spusti i ponovno ostavlja trag
#   a.setpos(x,y)   postavlja kornjacu na određenu oziciju u koordinatnom sustavu, a pritom OSTAVLJA trag


def kvadrat(n):  # funkcija kojoj crtamo kvadrat
    a.forward(n)
    a.right(90)
    a.forward(n)
    a.right(90)
    a.forward(n)
    a.right(90)
    a.forward(n)


def kružnica(n):  # funkcija crtanja kružnice i ispunjavanja unutrašnjosti bojom
    a.begin_fill()
    a.circle(n)
    a.end_fill()


def rand_kruznice(n):  # random crtanje n kruznica sa razlicitim radijusima i razlicitim bojama
    for i in range(n):
        randRadius = random.randrange(10, 80)
        rand1 = random.randrange(-200, 200)
        rand2 = random.randrange(-200, 200)
        randBoja = random.randrange(0, len(boje))
        # moze i random.choice(boje) zato što odmah bira boju
        randBoja2 = random.randrange(0, len(boje))
        a.penup()
        a.setpos(rand1, rand2)
        a.pendown()
        a.color(boje[randBoja], boje[randBoja2])
        a.begin_fill()
        a.circle(randRadius)
        a.end_fill()


turtle.done()
