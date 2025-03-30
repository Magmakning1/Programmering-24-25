import turtle

class Screen:

    def __init__(self, screensize: int, color):
        self.screensize = screensize
        self.colormode = 255
        self.color = color
        print(f"Screen made: size= {screensize}, colormode= {self.colormode}")

        self.screen = turtle.Screen()
        self.screen.setup(screensize, screensize)
        self.screen.screensize(screensize * 2, screensize * 2)
        self.screen.colormode(self.colormode)
        self.screen.bgcolor(self.color)

    def mainloop(self):
        while True:
            pass

class New_Turtle:

    def __init__(self, speed: int, color, pensize: int):
        self.speed = speed
        self.color = color
        self.pensize = pensize

        self.turtle = turtle.Turtle()
        self.turtle.speed(self.speed)
        self.turtle.pensize(self.pensize)
        self.turtle.color(self.color)
        pass

    def move(self, heading, distance):
        self.turtle.setheading(heading)
        self.turtle.forward(distance)

    def goto(self, x, y):
        self.turtle.goto(x,y)

    def tp(self, x, y):
        self.turtle.penup()
        self.turtle.goto(x,y)
        self.turtle.pendown()