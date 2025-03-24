import turtle

#screen
screensize = 600
screen = turtle.Screen()
screen.setup(screensize, screensize)
screen.screensize(screensize * 2, screensize * 2)
screen.colormode(255)
screen.bgcolor(0, 0, 0)


redt_aspect_ratio = (270, 160)

redt = turtle.Turtle()
redt.speed(0)
redt.pensize(5)
redt.color(255, 0, 0)
redt.hideturtle()

whitet = turtle.Turtle()
whitet.speed(0)
whitet.pensize(5)
whitet.color(255, 255, 255)
whitet.hideturtle()

bluet = turtle.Turtle()
bluet.speed(0)
bluet.pensize(3)
bluet.color(0, 0, 255)
bluet.hideturtle()

redt.penup()
redt.goto(-redt_aspect_ratio[0] / 2, redt_aspect_ratio[1])
redt.pendown()

whitet.penup()
whitet.goto(-redt_aspect_ratio[0] / 4, redt_aspect_ratio[1])
whitet.pendown()

bluet.penup()
bluet.goto(-redt_aspect_ratio[0] / 4 + 10, redt_aspect_ratio[1])
bluet.pendown()


for i in range(redt_aspect_ratio[0]):
    redt.goto(redt.xcor(), redt_aspect_ratio[1])
    redt.goto(redt.xcor() + 1, 0)

for i in range(int(redt_aspect_ratio[0] / 7)):
    whitet.pensize(7)
    whitet.goto(whitet.xcor(), redt_aspect_ratio[1])
    whitet.goto(whitet.xcor() + 1, 0)

whitet.penup()
whitet.pensize(5)
whitet.goto(-redt_aspect_ratio[0] / 2, int(redt_aspect_ratio[1] / 2) -20)
whitet.pendown()

for i in range(int(redt_aspect_ratio[0] / 7)):
    whitet.goto(redt_aspect_ratio[0] / 2, whitet.ycor())
    whitet.goto(-redt_aspect_ratio[0] / 2, whitet.ycor() + 1)

for i in range(int(redt_aspect_ratio[0] / 14)):
    bluet.pensize(5)
    bluet.goto(bluet.xcor(), redt_aspect_ratio[1])
    bluet.goto(bluet.xcor() + 1, 0)

bluet.penup()
bluet.pensize(3)
bluet.goto(-redt_aspect_ratio[0] / 2, int(redt_aspect_ratio[1] / 2) -12)
bluet.pendown()

for i in range(int(redt_aspect_ratio[0] / 12)):
    bluet.goto(redt_aspect_ratio[0] / 2, bluet.ycor())
    bluet.goto(-redt_aspect_ratio[0] / 2, bluet.ycor() + 1)

bt = turtle.Turtle()
bt.speed(0)
bt.hideturtle()
bt.color(0, 0, 0)
bt.pensize(7)

bt.penup()
bt.goto(int(-redt_aspect_ratio[0] / 2),int(redt_aspect_ratio[1]))
bt.pendown()

for i in range(2):
  bt.forward(redt_aspect_ratio[0])
  bt.right(90)
  bt.forward(redt_aspect_ratio[1])
  bt.right(90)

screen.mainloop()