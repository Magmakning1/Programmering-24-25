import turtle
import random

############variable bank##########
screensize = 800
colorRainbow = False
Tcolor = "white"  #only works if colorRainbow = False
borderbounce = True
speed = 10 # also known as jump distance
ishidden = False
truereset = True

############screensetup############
screen = turtle.Screen()
screen.setup(screensize, screensize)
screen.screensize(screensize * 2, screensize * 2)
screen.bgcolor("black")
turtle.colormode(255)

############Turlesetup#############
T = turtle.Turtle()
T.speed(0)
T.pensize(3)

if ishidden:
    T.hideturtle()
if not ishidden:
    T.showturtle()

T.penup()
if ishidden:
    T.pendown()

############inputs#################
def input_keyW():
    T.sety(T.ycor() + speed)
    T.setheading(90)
def input_keyD():
    T.setx(T.xcor() + speed)
    T.setheading(0)
def input_keyA():
    T.setx(T.xcor() - speed)
    T.setheading(180)
def input_keyS():
    T.sety(T.ycor() - speed)
    T.setheading(270)
def input_keyQ():
    T.penup()
    if ishidden:
        T.showturtle()
def input_keyE():
    T.pendown()
    if ishidden:
        T.hideturtle()
def input_keyR():
    T.clear()

#############borderdrawn###########
if borderbounce:
    bt = turtle.Turtle()
    bt.hideturtle()
    bt.speed(0)
    bt.penup()
    bt.goto(-screensize / 2, -screensize / 2)
    bt.pendown()
    bt.color("red")
    for i in range(4):
        bt.forward(screensize)
        bt.left(90)

#############mainloop##############
while True:
    if colorRainbow:
        T.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    else:
        T.color(Tcolor)

    if borderbounce:
        if T.xcor() > int(screensize / 2) or T.xcor() < int(-screensize / 2) or T.ycor() > int(screensize / 2) or T.ycor() < int(-screensize / 2):
            input_keyQ()
            if truereset:
                input_keyR()
            T.goto(0,0)

    screen.listen()
    screen.onkey(input_keyW, "w")
    screen.onkey(input_keyD, "d")
    screen.onkey(input_keyA, "a")
    screen.onkey(input_keyS, "s")
    screen.onkey(input_keyE, "e")
    screen.onkey(input_keyQ, "q")
    screen.onkey(input_keyR, "r")

    print(int(T.xcor()), "  ", int(T.ycor()))