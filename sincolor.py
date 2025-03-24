import turtle
import math
import random

screensize = 700
screen = turtle.Screen()
screen.setup(width=screensize, height=screensize)
screen.screensize(screensize * 2, screensize * 2)
screen.colormode(255)
screen.bgcolor(0, 0, 0)
scale = 10

colorshown = True

lowrand = 3 #min 1 maks 3
highrand = 3 # min 1 maks 3

color = [0, 0, 0]

sin1 = turtle.Turtle()
sin1.speed(0)
sin1.color(color)
sin1.pensize(5)
sin1.sety(-50)
sin1.setx(-screensize / 2)
x1 = 0

sin2 = turtle.Turtle()
sin2.speed(0)
sin2.color(color)
sin2.pensize(5)
sin2.sety(0)
sin2.setx(-screensize / 2)
x2 = 0

sin3 = turtle.Turtle()
sin3.speed(0)
sin3.color(color)
sin3.pensize(5)
sin3.sety(50)
sin3.setx(-screensize / 2)
x3 = 0

wt = turtle.Turtle()
wt.speed(0)
wt.pensize(5)

if colorshown:
    wt.penup()
    wt.goto(0,120)
    wt.pendown()
    wt.pensize(60)

if not colorshown:
    sin1.hideturtle()
    sin2.hideturtle()
    sin3.hideturtle()
    sin1.penup()
    sin2.penup()
    sin3.penup()

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
    print(wt.pensize())
def pensizedown():
    wt.pensize(wt.pensize() - 1)
    print(wt.pensize())

while True:
    sin1.goto((x1 / 10) * scale * 2 - (screensize / 2), math.sin(x1 / 10) * scale * 2 + 60)
    x1 += 1

    sin2.goto((x2 / 10) * scale * 2 - (screensize / 2), math.sin(x2 / 10) * scale * 2)
    x2 += 1

    sin3.goto((x3 / 10) * scale * 2 - (screensize / 2), math.sin(x3 / 10) * scale * 2 - 60)
    x3 += 1

    if sin1.xcor() > screensize / 2 or sin1.xcor() < -screensize / 2 or sin1.ycor() > screensize / 2 or sin1.ycor() < -screensize / 2:
        sin1.penup()
        sin1.setx(-screensize / 2)
        if colorshown:
            sin1.pendown()
        x1 = 0

    if sin2.xcor() > screensize / 2 or sin2.xcor() < -screensize / 2 or sin2.ycor() > screensize / 2 or sin2.ycor() < -screensize / 2:
        sin2.penup()
        sin2.setx(-screensize / 2)
        if colorshown:
            sin2.pendown()
        x2 = 0

    if sin3.xcor() > screensize / 2 or sin3.xcor() < -screensize / 2 or sin3.ycor() > screensize / 2 or sin3.ycor() < -screensize / 2:
        sin3.penup()
        sin3.setx(screensize / 2)
        if colorshown:
            sin3.pendown()
        x3 = 0

    sin1.color(abs(int(sin1.ycor() * random.randint(lowrand, highrand))), abs(int(sin2.ycor() * random.randint(lowrand, highrand))),
               abs(int(sin3.ycor() * random.randint(lowrand, highrand))))
    sin2.color(abs(int(sin1.ycor() * random.randint(lowrand, highrand))), abs(int(sin2.ycor() * random.randint(lowrand, highrand))),
               abs(int(sin3.ycor() * random.randint(lowrand, highrand))))
    sin3.color(abs(int(sin1.ycor() * random.randint(lowrand, highrand))), abs(int(sin2.ycor() * random.randint(lowrand, highrand))),
               abs(int(sin3.ycor() * random.randint(lowrand, highrand))))
    if colorshown:
        print(abs(int(sin1.ycor() * random.randint(lowrand, highrand))), abs(int(sin2.ycor() * random.randint(lowrand, highrand))),
              abs(int(sin3.ycor() * random.randint(lowrand, highrand))))

    wt.color(abs(int(sin1.ycor() * random.randint(lowrand, highrand))), abs(int(sin2.ycor() * random.randint(lowrand, highrand))),
             abs(int(sin3.ycor() * random.randint(lowrand, highrand))))

    if colorshown:
        wt.forward(1)
        wt.backward(1)

    if not colorshown:
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
