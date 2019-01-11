# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 13:54:42 2018

@author: Gebruiker
"""
import itertools 

##---TASK 7.2: USING CLASSES TO DEFINE ATTRIBUTES AND METHODS OF MOVING FIGURES----------------------------
#from Shapes import *
#from pylab import random as r
#
#
#class Moving_shape:
#    """
#        class for moving shapes.
#       
#    """
#    
#    def __init__(self,frame,shape,diameter):
#        ran_gen = r()
#        self.shape = shape
#        self.diameter = diameter
#        self.figure = Shape(shape, diameter)
#        
#        self.minx,self.maxx = self.minx_and_maxx_calc(frame)
#        self.y = self.minx + r() * (self.maxx - self.minx)
#        self.x = self.minx + r() * (self.maxx - self.minx)
#        if ran_gen<0.5:        
#            self.dx = (5 + 10*-ran_gen)
#            self.dy = (5 + 10*-ran_gen)
#        else:
#            self.dx = (5 + 10*ran_gen) 
#            self.dy = (5 + 10*ran_gen)
#    
#    def goto(self, x, y):
#        """
#             moves the shape across the plot.
#        """
#        self.figure.goto(x,y)
#        
#    def moveTick(self): 
#        """
#            updates x and y coordinates and envokes goto method.
#            
#        """
#        ran_gen = r()      
#        self.x += self.dx
#        self.y += self.dy
#        self.x = self.make_shape_bounce_x(ran_gen)
#        self.y = self.make_shape_bounce_y(ran_gen)
#        self.figure.goto(self.x,self.y)
#     
#    
#    def minx_and_maxx_calc(self, frame):
#        """
#            creates a minimum value for x and y to prevent shapes
#            overlapping the boundary.
#        
#        """
#        self.maxx = frame.width - self.diameter/2
#        self.minx =  self.diameter/2
#        return self.minx, self.maxx
#
#        
#    def make_shape_bounce_x(self, ran_gen):
#        """
#            uses conditionals to decide if shape is reaching top or 
#            bottom boundary and send shape in opposite direction.
#            
#        """
## minimum x-boarder 
#        if (self.x <= self.minx):
#            self.dx = (5 + 10*ran_gen)
#            self.x += self.dx
#            
#            return self.x
## maximum x-boarder
#        elif (self.x >= self.maxx):
#            self.dx = (-5 + 10*-ran_gen)
#            self.x += self.dx
#            return self.x
#        else:
#            return self.x
#        
#    def make_shape_bounce_y(self, ran_gen):
#        """
#            uses conditionals to decide if shape is reaching left or 
#            right boundary and send shape in opposite direction.
#            
#        """
## minimum y-boarder
#        if (self.y <= self.minx):
#            self.dy = (5 + 10*ran_gen)
#            self.y += self.dy
#            return self.y
## maximum y-boarder
#        elif (self.y >= self.maxx):
#            self.dy = (-5 + 10*-ran_gen)
#            self.y += self.dy
#            return self.y
#        else:
#            return self.y
#            
#        
#class Square(Moving_shape):
#    """
#        class square is a subclass of Moving_shape.
#        square's init method invokes the parent class init method.
#        
#    """
#    def __init__(self,frame,diameter):
#        Moving_shape.__init__(self,frame,"square",diameter)
#
#
#class Diamond(Moving_shape):
#    """
#        class diamond is a subclass of Moving_shape.
#        Diamond's init method invokes the parent class init method.
#        To ensure the diamond shape stays within the border, a sep  minx_maxx
#        function is provided, which overrides the same function given in           
#        parent class shapes.
#
#        
#    """
#    def __init__(self,frame,diameter):
#        Moving_shape.__init__(self,frame,"diamond",diameter)
#    
#    def minx_and_maxx_calc(self, frame):
#        self.maxx = frame.width - self.diameter
#        self.minx =  self.diameter
#        return self.minx, self.maxx
#
#    
#class Circle(Moving_shape):
#    """
#        class circle is a subclass of Moving_shape.
#        Circle's init method invokes the parent class init method.
#        
#    """
#    def __init__(self,frame,diameter):
#        Moving_shape.__init__(self,frame,"circle",diameter)
        

#EXTENSION VERSION

from Shapes import *
from pylab import random as r


class Moving_shape:
    """
        class for moving shapes.
       
    """
    
    def __init__(self,frame,shape,diameter):
        ran_gen = r()
        self.shape = shape
        self.diameter = diameter
        self.figure = Shape(shape, diameter)
        
        self.minx,self.maxx = self.minx_and_maxx_calc(frame)
        self.y = self.minx + r() * (self.maxx - self.minx)
        self.x = self.minx + r() * (self.maxx - self.minx)
        if ran_gen<0.5:        
            self.dx = (5 + 10*-ran_gen)
            self.dy = (5 + 10*-ran_gen)
        else:
            self.dx = (5 + 10*ran_gen) 
            self.dy = (5 + 10*ran_gen)
    
    def goto(self, x, y):
        """
             moves the shape across the plot.

        """
        
        self.figure.goto(x,y)
        
        
    def moveTick(self, shapes): 
        """
            updates x and y coordinates and envokes goto method.
            
        """
        ran_gen = r()
        
        
        

        for j in range(len(shapes)):
            current = shapes[j]
            for k in range(len(shapes)):
                if current != shapes[k]:
                    current.check_collide(shapes[k])
        
        self.x = self.make_shape_bounce_x(ran_gen)
        self.y = self.make_shape_bounce_y(ran_gen)

        

        self.figure.goto(self.x,self.y)
        
    def check_collide(self, other):
        self.x += self.dx
        self.y += self.dy
        diff_between_x = abs(self.x - other.x)  
        diff_between_y = abs(self.y - other.y)  
        
        if (self.diameter>= diff_between_x) and     (self.diameter>= diff_between_y):
            self.dx = -self.dx
            self.x += self.dx
            self.dy = -self.dy
            self.y += self.dy

            
        
            
        
        
                
    def minx_and_maxx_calc(self, frame):
        """
            creates a minimum value for x and y to prevent shapes
            overlapping the boundary.
        
        """
        self.maxx = frame.width - self.diameter/2
        self.minx =  self.diameter/2
        return self.minx, self.maxx

        
    def make_shape_bounce_x(self, ran_gen):
        """
            uses conditionals to decide if shape is reaching top or 
            bottom boundary and send shape in opposite direction.
            
        """
# minimum x-boarder 
        if (self.x <= self.minx):
            self.dx = (5 + 10*ran_gen)
            self.x += self.dx
            
            return self.x
# maximum x-boarder
        elif (self.x >= self.maxx):
            self.dx = (-5 + 10*-ran_gen)
            self.x += self.dx
            return self.x
        else:
            return self.x
        
    def make_shape_bounce_y(self, ran_gen):
        """
            uses conditionals to decide if shape is reaching left or 
            right boundary and send shape in opposite direction.
            
        """
# minimum y-boarder
        if (self.y <= self.minx):
            self.dy = (5 + 10*ran_gen)
            self.y += self.dy
            return self.y
# maximum y-boarder
        elif (self.y >= self.maxx):
            self.dy = (-5 + 10*-ran_gen)
            self.y += self.dy
            return self.y
        else:
            return self.y
            
    
        
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
        To ensure the diamond shape stays within the border, a sep  minx_maxx
        function is provided, which overrides the same function given in           
        parent class shapes.
    """
    def __init__(self,frame,diameter):
        Moving_shape.__init__(self,frame,"diamond",diameter)
    
    def minx_and_maxx_calc(self, frame):
        self.maxx = frame.width - self.diameter
        self.minx =  self.diameter
        return self.minx, self.maxx

    
class Circle(Moving_shape):
    """
        class circle is a subclass of Moving_shape.
        Circle's init method invokes the parent class init method.
        
    """
    def __init__(self,frame,diameter):
        Moving_shape.__init__(self,frame,"circle",diameter)





