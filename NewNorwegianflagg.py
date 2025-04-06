from Turtle_custom import *

scr = Screen(400,[0, 0, 0])
t1 = Turtle(0, [255, 0, 0], 5, True)
t2 = Turtle(0, [255, 255, 255], 5, True)
t3 = Turtle(0, [0, 0, 255], 5, True)
t4 = Turtle(0, [255, 255, 255], 5, True)

t1.tp(-135,-80)
for i in range(135):
    t1.move(90, 160)
    print(int(t1.xcor()), " ", int(t1.ycor()))
    t1.move(0,2)
    t1.move(270, 160)
    print(int(t1.xcor()), " ", int(t1.ycor()))

t2.tp(-135 / 2, -80)
for i in range(20):
    t2.move(90, 160)
    print(int(t2.xcor()), " ", int(t2.ycor()))
    t2.move(0,2)
    t2.move(270, 160)
    print(int(t2.xcor()), " ", int(t2.ycor()))
t2.tp(-135, 80 / 5)
for i in range(20):
    t2.move(0, 270)
    print(int(t2.xcor()), " ", int(t2.ycor()))
    t2.move(270,2)
    t2.move(180, 270)
    print(int(t2.xcor()), " ", int(t2.ycor()))

t3.tp(-135 / 2.3, -80)
for i in range(12):
    t3.move(90, 160)
    print(int(t3.xcor()), " ", int(t3.ycor()))
    t3.move(0,2)
    t3.move(270, 160)
    print(int(t3.xcor()), " ", int(t3.ycor()))
t3.tp(-135, 80 / 10)
for i in range(12):
    t3.move(0, 270)
    print(int(t3.xcor()), " ", int(t3.ycor()))
    t3.move(270,2)
    t3.move(180, 270)
    print(int(t3.xcor()), " ", int(t3.ycor()))

t4.tp(-135, 80)
t4.move(0, 270)
t4.move(270, 160)
t4.move(180, 270)
t4.move(90, 160)


scr.mainloop()