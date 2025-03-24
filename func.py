import turtle
import math

#Screensetup
screensize = 700 * 2
screen= turtle.Screen()
screen.setup(width=screensize / 2, height=screensize / 2)
screen.screensize(screensize * 2, screensize * 2)
screen.bgcolor("black")
screen.title("Turtle test")
MAGNIFICATION = 2
speed = 1

#Turtle and Borderdrawn
t = turtle.Turtle()
t.speed(0)
t.pensize(0)
t.color("white")
boundary_x = screensize / 2
boundary_y = screensize / 2
boundary_nx = -screensize / 2
boundary_ny = -screensize / 2
borderdrawn = False
bt = turtle.Turtle()
bt.speed(0)
bt.pensize(0)
bt.color("black")
if borderdrawn:
  bt.goto((-screensize / 2),(screensize / 2))
  bt.color("red")
  borderdrawn1 = 0
  while borderdrawn1 <= 4:
    bt.forward(screensize)
    bt.right(90)
    borderdrawn1 += 1

print_cord = True
def cords():
  print(t.xcor(), t.ycor())

def rainbow_color():
  colors = ["red", "orange", "yellow", "green", "blue", "purple","white","grey"]
  current_color = getattr(rainbow_color, 'current_index', 0)
  t.color(colors[current_color])
  turtle.color(colors[current_color])
  rainbow_color.current_index = (current_color + 1) % len(colors)

progress1 = 1
progress2 = 1

interval = screensize / 50
t.hideturtle()
bt.hideturtle()
t.penup()
bt.penup()
b1 = turtle.Turtle()
b1.speed(0)
b1.color("grey")
b1.hideturtle()

b2 = turtle.Turtle()
b2.speed(0)
b2.color("grey")
b2.hideturtle()
screen.bgcolor("black")


def turtle_up():
  global progress1
  b1.color("grey")
  b1.penup()
  b1.setx(-screensize)
  b1.sety(-screensize)
  b1.pendown()
  b1.setheading(90)
  b1.forward(interval * progress1)
  b1.setheading(0)
  b1.forward(screensize * 2)
  progress1 += 1

def turtle_side():
  global progress2
  b2.color("grey")
  b2.penup()
  b2.setx(-screensize)
  b2.sety(-screensize)
  b2.pendown()
  b2.setheading(0)
  b2.forward(interval * progress2)
  b2.setheading(90)
  b2.forward(screensize * 2)
  progress2 += 1

def turtle_cross():
  b1.setx(0)
  b1.sety(0)
  b1.pensize(3)
  b1.color("white")
  for i in range(4):
    b1.left(90)
    b1.forward(screensize)
    b1.left(180)
    b1.forward(screensize)

for i in range(100):
  turtle_up()
  turtle_side()
turtle_cross()

b2speed = 0
b2 = turtle.Turtle()
b2.speed(b2speed)
b2.color("purple")
b2.pensize(3)
b2.hideturtle()
starting = int(math.sqrt(screensize * 2))
squere_factor1 = 3
squere_factor2 = 2
scale = 10

squere1 = True
squere2 = True
sin = True
tan = False
cos = True
quadratic = False

if squere1:
  if squere_factor1 % 2  == 0 :
    b2.color("purple")
    b2.penup()
    b2.speed(0)
    b2.goto(-starting * scale, starting**squere_factor1)
    b2.speed(b2speed)
    b2.pendown()
  else:
    b2.penup()
    b2.speed(0)
    b2.goto(-starting * scale, -starting**squere_factor1)
    b2.speed(b2speed)
    b2.pendown()

  for x in range(-starting, starting + 1, 1):
    print(x, "  ", x**squere_factor1)
    b2.goto(x * scale, x**squere_factor1)

if squere2:
  if squere_factor2 % 2  == 0 :
    b2.color("red")
    b2.penup()
    b2.speed(0)
    b2.goto(-starting * scale, starting**squere_factor2)
    b2.speed(b2speed)
    b2.pendown()
  else:
    b2.penup()
    b2.speed(0)
    b2.goto(-starting * scale, -starting**squere_factor2)
    b2.speed(b2speed)
    b2.pendown()

  for x in range(-starting, starting + 1, 1):
    print(x, "  ", x**squere_factor2)
    b2.goto(x * (scale / 2), x**squere_factor2)

if sin:
  b2.color("green")
  b2.speed(0)
  b2.pensize(3)
  b2.penup()
  b2.goto(-starting * scale, 0)
  b2.pendown()
  for x in range(-starting * 10, starting * 10 + 1, 1):
    print(math.sin(x / 10))
    b2.goto((x / 10) * scale * 2, (math.sin(x / 10) * scale) * 3 )


if tan:
  b2.color("orange")
  b2.speed(0)
  b2.pensize(3)
  b2.penup()
  b2.goto(-starting * scale, 0)
  b2.pendown()
  for x in range(-starting * 10, starting * 10 + 1, 1):
    print(math.tan(x))
    b2.goto(x * scale, math.tan(x))

if cos:
  b2.color("blue")
  b2.speed(0)
  b2.pensize(3)
  b2.penup()
  b2.goto(-starting * scale, 0)
  b2.pendown()
  for x in range(-starting * 10, starting * 10 + 1, 1):
    print(math.cos(x / 10))
    b2.goto(x / 10 * scale * 2, (math.cos(x / 10) * scale) * 3 )

if quadratic:
  b2.color("yellow")
  b2.speed(0)
b1 = turtle.Turtle()
b1.speed(0)
b1.color("grey")
b1.hideturtle()
screen.bgcolor("black")
for x in range(0,21, 1):
  print(x, "  ",x**x, "       ")
  b2.goto(x * scale, x**x)

screen.mainloop()