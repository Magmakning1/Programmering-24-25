from Turtle_custom import *

scr = Screen(400,[255, 255, 255])
scr.color = [255, 255, 255]

T = New_Turtle(2, [0, 0, 0], 5)
T.move(90, 200)
T.goto(200, 200)
T.tp(-200, -200)

scr.mainloop()