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
        print(f"New turtle created: speed= {self.speed} color= {self.color} pensize= {self.pensize}")
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

    def xcor(self):
        return self.turtle.xcor()

    def ycor(self):
        return self.turtle.ycor()

    def heading(self):
        return self.turtle.heading()

    def return_00(self, screensize):
        
          if self.xcor() > screensize / 2 or self.xcor() < -screensize / 2 or self.ycor() > screensize / 2 or self.ycor() < -screensize / 2:
              self.tp(0,0)
    def info(self):
        print(int(self.xcor()), int(self.ycor()))