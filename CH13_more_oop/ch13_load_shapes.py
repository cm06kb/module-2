


#----------------TASK 7.1: MAKE FIRST MOVING FIGURE----------------------------
from Shapes import *
from pylab import random as r
"""
    creates an instance of the Frame class and opens a graphics window.
    
"""
frame = Frame()

"""
    creates an object of the Shape class which is assigned to s1.
    Shape class takes two parameters 
    1. shape (this can be square, circle or diamond) 
    2. diameter

"""
s1 = Shape("square", 100)

"""
    calls the figure's goto method, this moves the figure to specified coordinates.
    so the square moves from 0,0 to 200 on x axis and 100 on the y.    

"""
s1.goto(200,100)


"""
    Animates square object. 
    set x and y coordinates to 0.
    use a for loop to change x and y with time, causing the shape to move on the plot.
"""
x = 0
y = 0

for i in range(100):
    s1.goto(x,y)
    x = x + 5
    y = y + 5
    


























