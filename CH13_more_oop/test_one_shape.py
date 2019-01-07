
from MovingShapes import *
"""
    this code tests the code in the MovingShapes file by creating an instance of square.
    When then attempt to move this instance.
"""
frame = Frame()
shape1 = Square(frame, 100)
for i in range(100):
    shape1.moveTick()

