# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 14:56:08 2018

@author: Gebruiker
"""

from MovingShapes_extension import *
"""
    call frame method with grid set to 300 by 300.
    
"""
frame = Frame(300, 300)
"""
total shapes to plot is 2

"""
numshapes = 1

"""
for loop below calls the square class with arguments frame and diameter
and appends the square produce to the shapes list.This loops for the range of numshapes - 3 times.
"""

shapes = []

for i in range(numshapes):
    shapes.append(Circle(frame, 30))
    shapes.append(Circle(frame, 30))
    shapes.append(Circle(frame, 30))


    


    

"""
nested for loop.
innner for loop iterates over shapes (loops 3 times).
with each iteration movTick method is invoked. 
Outer for loop makes inner for loop repeat 100 times.
This creates movement of the three squares on the grid.

"""

#
#        
#

for i in range(200):
    for shape in shapes:
        shape.moveTick(shapes)
            
            










