# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 13:54:42 2018

@author: Gebruiker
"""

#---TASK 7.2: USING CLASSES TO DEFINE ATTRIBUTES AND METHODS OF MOVING FIGURES----------------------------
from Shapes import *
from pylab import random as r

class Moving_shape:
    """
        class for moving shapes.
        goto method-moves the shape across the plot.
        moveTick method - updates x and y coordinates and envokes
        goto method.
    """
  
    
    def __init__(self,frame,shape,diameter):
        ran_gen = r()
        self.shape = shape
        self.diameter = diameter
        self.figure = Shape(shape, diameter)
        self.maxx = frame.width - diameter/2
        self.minx =  diameter/2
        self.y = self.minx + r() * (self.maxx - self.minx)
        self.x = self.minx + r() * (self.maxx - self.minx)
        
        if ran_gen<0.5:        
            self.dx = (5 + 10*-ran_gen)
            self.dy = (5 + 10*-ran_gen)
        else:
            self.dx = (5 + 10*ran_gen) 
            self.dy = (5 + 10*ran_gen)
    
    
    
    def goto(self, x,y):
        self.figure.goto(x,y)
    def moveTick(self):  
        ran_gen = r()      
        self.x += self.dx
        self.y += self.dy
    
   

# minimum x-boarder        
        if (self.x <= self.minx):
            self.dx = (5 + 10*ran_gen)
            self.x += self.dx
# maximum x-boarder
        elif (self.x >= self.maxx):
            self.dx = (-5 + 10*-ran_gen)
            self.x += self.dx
# minimum y-boarder
        if (self.y <= self.minx):
            self.dy = (5 + 10*ran_gen)
            self.y += self.dy
# maximum y-boarder
        elif (self.y >= self.maxx):
            self.dy = (-5 + 10*-ran_gen)
            self.y += self.dy
            
        self.figure.goto(self.x,self.y)
    
class Square(Moving_shape):
    """
        class square is a subclass of Moving_shape.
        square's init method invokes the parent class init method.
        
    """
    def __init__(self,frame,diameter):
        Moving_shape.__init__(self,frame,"square",diameter)


class Diamond(Moving_shape):
    """
        class diamond is a subclass of Moving_shape.
        Diamond's init method invokes the parent class init method.

        
    """
    def __init__(self,frame,diameter):
        Moving_shape.__init__(self,frame,"diamond",diameter)
    def min_and_max():
        self.maxx = frame.width - diameter
        self.minx =  diameter

    
class Circle(Moving_shape):
    """
        class circle is a subclass of Moving_shape.
        Circle's init method invokes the parent class init method.
        
    """
    def __init__(self,frame,diameter):
        Moving_shape.__init__(self,frame,"circle",diameter)
        

        





