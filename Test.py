import turtle
import math

class Triangle:
    def __init__(self,sides,xpos,ypos,size,rotation,pensize):
        self.sides = sides
        self.xpos = xpos
        self.ypos = ypos
        self.size = size
        self.rotation = rotation
        self.pensize = pensize
    def drawTriangleGOOD(self):
        x = turtle.Turtle()
        x.goto(self.xpos,self.ypos)
        x.speed(0)
        x.hideturtle()
        x.pensize(self.pensize)
        x.right(30+self.rotation)
        x.penup()
        x.forward(self.size)
        x.left(150)
        x.pendown()
        for i in range(3):
            x.forward(2*self.size*math.cos(30*math.pi/180))
            x.left(120)
        x.penup()
        x.goto(self.xpos,self.ypos)
        turtle.done()

    def drawTriangleBAD(self):
        angleChange = 360/self.sides
        x = turtle.Turtle()
        x.penup()
        startAngle = 90+self.rotation
        xCal = self.size*(math.cos((startAngle)*(math.pi/180)))
        yCal = self.size*(math.sin((startAngle)*(math.pi/180)))
        x.goto(xCal,yCal)
        x.pendown()

        for i in range(self.sides+1):
            startAngle = 90+self.rotation+(angleChange*i)
            xCal = self.size*(math.cos((startAngle)*(math.pi/180)))
            yCal = self.size*(math.sin((startAngle)*(math.pi/180)))
            x.goto(xCal,yCal)
        turtle.done()
