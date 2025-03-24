import turtle
import random
import math

debugmode = False
sin_instead_of_random = False
color_test = True #Deactivated automaticly when debugmode = True

#screen
screensize = 700
screen= turtle.Screen()
screen.setup(width=screensize, height=screensize)
screen.screensize(screensize * 2, screensize * 2)
screen.bgcolor(0,0,0)
screen.colormode(255)
angles = ["0", "90", "180", "270"]

#Turtles
bt1 = turtle.Turtle()
bt1.speed(0)
bt1.hideturtle()
bt1.color(255,255,255)

bt2 = turtle.Turtle()
bt2.speed(0)
bt2.hideturtle()
bt2.color(255,0,0)

ct= turtle.Turtle()
ctspeed = 5
ct.speed(0)
ct.pensize(2)
ct.hideturtle()
ct.penup()
ctvalue3 = random.randint(0,255)
random.seed(ctvalue3)
ct.setheading(int(random.choice(angles)))

wt = turtle.Turtle()
wt.speed(0)
wt.pensize(5)
if debugmode:
    wt.goto(-screensize / 2, -screensize / 2)

b2speed = 0
b2 = turtle.Turtle()
b2.speed(b2speed)
b2.pensize(3)

if not debugmode:
    b2.hideturtle()

starting = int(math.sqrt(screensize * 2))
scale = 10
b2.speed(0)
b2.pensize(3)
x = 1

#startup
if debugmode:
    border = True
    ct_show = True
    color_test = False

if not debugmode:
    border = False
    ct_show = False

if ct_show:
    bt1.penup()
    bt1.goto(-245, -245)
    bt1.pendown()
    for i in range(4):
        bt1.forward(245 * 2)
        bt1.left(90)

if border:
    bt2.penup()
    bt2.goto(-screensize / 2, -screensize / 2)
    bt2.pendown()
    for i in range(4):
        bt2.forward(screensize)
        bt2.left(90)

if not debugmode:
    b2.penup()

def upword():
    wt.sety(wt.ycor() + 10)
    wt.setheading(90)
def rightword():
    wt.setx(wt.xcor() + 10)
    wt.setheading(0)
def leftword():
    wt.setx(wt.xcor() - 10)
    wt.setheading(180)
def downword():
    wt.sety(wt.ycor() - 10)
    wt.setheading(270)
def reset():
    wt.clear()
def penup():
    wt.penup()
def pendown():
    wt.pendown()
def pensizeup():
    wt.pensize(wt.pensize() + 1)
def pensizedown():
    wt.pensize(wt.pensize() - 1)

#mainloop
while True:
    ct.forward(ctspeed)
    ct.left(random.randint(-20, 20))
    if ct_show:
        ct.showturtle()
        ct.pendown()

    if int(ct.xcor()) > int(245) or int(ct.xcor()) < int(-245) or int(ct.ycor()) > int(
            245) or int(ct.ycor()) < int(-245):
        ct.backward(ctspeed * 10)
        ct.left(180)

    colorcord1 = ct.xcor()
    colorcord2 = ct.ycor()
    if sin_instead_of_random:
        colorcord3 = abs(int(b2.ycor() * 10))
    if not sin_instead_of_random:
        colorcord3 = ctvalue3

    ct.color(abs(int(colorcord1)), abs(int(colorcord2)), abs(int(colorcord3)))
    wt.color(abs(int(colorcord1)), abs(int(colorcord2)), abs(int(colorcord3)))
    b2.color(abs(int(colorcord1)), abs(int(colorcord2)), abs(int(colorcord3)))

    if border:
        if int(wt.xcor()) > int(screensize / 2) or int(wt.xcor()) < int(-screensize / 2) or int(wt.ycor()) > int(
                screensize / 2) or int(wt.ycor()) < int(-screensize / 2):
            wt.penup()
            wt.goto(0, 0)
            wt.pendown()

    if int(b2.xcor()) > int(screensize / 2) or int(b2.xcor()) < int(-screensize / 2) or int(b2.ycor()) > int(
            screensize / 2) or int(b2.ycor()) < int(-screensize / 2):
        b2.penup()
        b2.setx(0)
        x = 0
        if debugmode:
            b2.pendown()

    if sin_instead_of_random:
        b2.goto((x / 10) * scale * 2, math.sin(x / 10) * scale * 2)
        x += 1

    if color_test:
        wt.pensize(600)
        wt.forward(1)
        wt.backward(1)

    if debugmode:
        wt.hideturtle()
        wt.pensize(75)
        wt.forward(screensize)
        wt.left(90)

    if wt.pensize() <= 0:
        wt.pensize(1)

    if not debugmode or color_test:
        screen.listen()
        screen.onkey(upword, "w")
        screen.onkey(rightword, "d")
        screen.onkey(leftword, "a")
        screen.onkey(downword, "s")
        screen.onkey(penup, "q")
        screen.onkey(pendown, "e")
        screen.onkey(reset, "r")
        screen.onkey(pensizeup, "j")
        screen.onkey(pensizedown, "h")

    print(abs(int(colorcord1)), " ", abs(int(colorcord2)), " ", abs(int(colorcord3)), "   ", wt.pos(), " ",abs(int(b2.ycor() * 10))," ", wt.pensize())