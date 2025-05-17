import turtle as t

t1 = t.Turtle()
t1.speed(0)
t1.pensize(5)
t1.hideturtle()
segments = 36

#def funksjoner
def t1tp(x,y):
  t1.penup()
  t1.goto(x,y)
  t1.pendown()

def line(linestart, endline, linewith, linecolor):
  t1tp(linestart[0],linestart[1])
  t1.color(linecolor)
  t1.pensize(linewith)
  t1.goto(endline[0],endline[1])

def head(R,G,B):
  if R > 255:
    R = 255
  if G > 255:
    G = 255
  if B > 255:
    B = 255
  t1.color(abs(R),abs(G),abs(B))

  t1.begin_fill()
  for i in range(int(segments)):
    t1.forward(360 / int(segments))
    t1.left(360 / int(segments))
  t1.end_fill()

def eye(x,y,eyesize):
  t1tp(x,y)
  t1.pensize(eyesize * 10)
  t1.color(0,0,0)
  t1.forward(1)
  t1tp(x,y)

  t1tp(x,y)
  t1.pensize(eyesize * 10 / 1.1)
  t1.color(255,255,255)
  t1.forward(1)
  t1tp(x,y)

  t1tp(x,y)
  t1.pensize(eyesize * 10 / 3)
  t1.color(0,0,0)
  t1.forward(1)
  t1tp(x,y)

def outline_circle(start_x,start_y, outline_size, color):
  t1tp(start_x,start_y)
  t1.pensize(outline_size)
  t1.color(color)
  for x in range(segments):
    t1.forward(360 / segments)
    t1.left(360 / segments)

def mtcs36(stmt, startpoint, penwith, color, clockwise, isFilling):
  t1tp(startpoint[0],startpoint[1])
  t1.color(color)
  t1.pensize(penwith)
  if isFilling:
    t1.begin_fill()
  for x in range(stmt):
    t1.forward(10)
    if clockwise:
      t1.right(10)
    if not clockwise:
      t1.left(10)
  if isFilling:
    t1.end_fill()

#faktiske tegning / bruk av def funksjonene
if True:
  head(255,242,209)
  eye(-20,60,4)
  eye(30,60,4)
  outline_circle(0,0,5,[0,0,0])
  line([-5,30],[15,30],15,[0,0,0])
  line([-35,74],[-5,71],7,[0,0,0])
  line([45,74],[15,71],7,[0,0,0])
  mtcs36(11,[0,0],5,[0,0,0],False, False)
  mtcs36(12,[t1.xcor(),t1.ycor()],5,[0,0,0],False, True)
  t1tp(0,0)
  line([5,-1],[5,-5],10,[0,0,0])
