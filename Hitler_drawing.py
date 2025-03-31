import turtle as t
import math

t1 = t.Turtle()
t1.speed(0)
t1.pensize(3)

def t1tp(x, y):
  t1.penup()
  t1.goto(x, y)
  t1.pendown()

def eye():
  t1.pensize(10)
  t1.forward(1)
  t1.pensize(3)

t1.begin_fill()
t1.color(245,245,220)
for i in range(36):
  t1.forward(10)
  t1.left(10)
t1.end_fill()
t1.color(0,0,0)
t1tp(-40, 90)
t1.setheading(330)

for i in range(10):
  t1.forward(11)
  t1.left(3)

t1.begin_fill()
t1.setheading(85)
for i in range(15):
  t1.left(10)
  t1.forward(10)
t1.end_fill()

t1.setheading(0)
t1tp(-20, 50)
eye()
t1tp(25, 50)
eye()

t1.pensize(6)
t1tp(0,30)
t1.forward(10)
t1.goto(0, 26)
t1.forward(10)

t1tp(0,0)
t1.setheading(270)
t1.forward(100)

t1.left(20)
t1.forward(100)
t1tp(0,-100)

t1.right(40)
t1.forward(100)
t1tp(0,0)

t1.right(90)
t1.forward(100)
t1tp(0,0)

t1tp(0,0)
t1.setheading(300)
t1.forward(20)
t1.pensize(7)
t1.color(255,0,0)
t1.forward(20)
t1.color(0,0,0)
t1.pensize(5)
t1.forward(60)
t1tp(0,90)

