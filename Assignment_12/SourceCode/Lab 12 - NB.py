########################################################################
##
## CS 101 Lab
## Program 12
## Nathan Bright
## nwbbdf@umsystem.edu
##
## PROBLEM: Use the turtle module to draw basic shapes.
##
## ALGORITHM: 
##      1. Code a class which draws a single point.
##      2. Make subclasses which either draw a circle or box.
##      3. Make subclasses of those subclasses which fill in the afformentioned circle or box.
## 
## ERROR HANDLING:
##      
## OTHER COMMENTS:
##      
##
########################################################################

import turtle

class Point(object):

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        #Basic draw handling, puts the pen to the digital paper.
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.color(self.color)
        turtle.setheading(0)
        self.draw_action()

    def draw_action(self):
        #Draws a singular point.
        turtle.dot()

class Box(Point):
    def __init__(self, x1, y1, width, height, color):
        super().__init__(x1, y1, color)
        self.width = width
        self.height = height
        self.color = color
    
    def draw_action(self):
        #Draws a box
        turtle.forward(self.width)
        turtle.right(90)
        turtle.forward(self.height)
        turtle.right(90)
        turtle.forward(self.width)
        turtle.right(90)
        turtle.forward(self.height)

class BoxFilled(Box):
    def __init__(self, x1, y1, width, height, color, fillcolor):
        super().__init__(x1, y1, width, height, color)
        self.fillcolor = fillcolor

    def draw_action(self):
        #Fills and draws a box.
        turtle.fillcolor(self.fillcolor)
        turtle.begin_fill()
        Box.draw_action(self)
        turtle.end_fill()

class Circle(Point):
    def __init__(self, x1, y1, radius, color):
        super().__init__(x1, y1, color)
        self.radius = radius
    
    def draw_action(self):
        #Generates a circle.
        turtle.circle(self.radius)

class CircleFilled(Circle):
    def __init__(self, x1, y1, radius, color, fillcolor):
        super().__init__(x1, y1, radius, color)
        self.fillcolor = fillcolor

    def draw_action(self):
        #Generates a filled circle.
        turtle.fillcolor(self.fillcolor)
        turtle.begin_fill()
        Circle.draw_action(self)
        turtle.end_fill()
