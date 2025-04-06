from Turtle_custom import *
import time

scr = Screen(700, [0,0,0])
t1 = Turtle(0, [255, 255, 255], 3, False)
while True:
    t1.move(t1.heading() + 1, 1)