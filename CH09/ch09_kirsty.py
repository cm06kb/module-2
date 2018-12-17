# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 09:28:48 2018

@author: Gebruiker
"""

#my_favourite_fruits = ["apples", "orange", "banana"]
#
#x = ["this", 55, "that",my_favourite_fruits]
#
#print(x[0], x[1], x[2], x[-1][-1])
#
#
#x.remove(my_favourite_fruits)
#print(x)
#
#x[1] = "and"
#print(x)
#x.append("again")
#print(x)
#
#
#x = ["the", "cat", "sat"]
#
#y = ["on", "the", "mat"]
#
#z = x + y
#print(z)
#
#
#print(set(x+y))

#x = ["this", "and", "that", "once", "again"]
#print(x)
#print(x[1:4])
#print(x[2::])

#x = [7, 11, 3, 9,2]
#print(x)
#print(sorted(x))
#print(sorted(x, reverse = False))
#print(x)
#x = [7, 11, 3, 9,2]
#x.sort()
#print(x)

#x = [ "cd", "ab", "gy", "fy", "ee"]
#print(x)
#print(sorted(x))
#print(sorted(x, reverse = False))
#print(x)
#x.sort()
#print(x)
#
#
#a = [0,1,2,3,4,5,6,7,8,9]
#print(a)
#del a[-1]
#print(a)
#""" removes the last element in the list, the original list has been altered"""
#a.pop(-1)
#print(a)
#"""removes the last item in the list, original list has been altered"""
#a.append("z")
#print(a)
#"""append adds an element to the end of the list"""
#
#b =(0,1,2,3,4,5,6,7,8,9)
#print(b)
##b[0] = 51
##del b[-1]
##b.pop(-1)
##b.append("z")
#"""cannot delete, pop elements, switch or append to a  tuple.They are immutable"""

a = [50,1,2,3,4,5,6,7,8,9]
b = (0,1,2,34,5,6,78,9)
c = (2,2,3,3,4,5,6,7,8,9)
my_favourite_fruits = ["apple", "oranges", "pears"]
x =["yw", "zs", "cs", "hd", "ab"]
y = ["ab", "cs", "hd", "yw", "zs"]
z = ["zs", "yw", "hd", "cs", "ab"]

y[0] = "zz"
y[-2] = "sd"

x2 = [("A", 3, z), ("c",1,y), ("b", 5, x)]

print(sorted(x2, key=lambda s:s[2][1][1]))


#x2 = [("a", 3, z), ("c",1,y), ("b", 5, x)]
#"""s represent each tuple, x2 tuples are sorted by item with index 0"""
#print(sorted(x2, key=lambda s:s[1]))
#"""sorting by  letter a """
#print(sorted(x2, key = lambda s:s[2][1]))
#"""sorting by number 1 """


























