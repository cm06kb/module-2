#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 17:18:12 2018

@author: Gebruiker
"""
"""task 1"""
print(5 - 6)
print(8 * 9)
print(6 / 2)
print(5 / 2)
print( 5.0 / 2)
print(5 % 2)
print(2 * (10 + 3))
print(2 ** 4)
 
"""Task 2 variable practise."""
age = 5
age = "almost three"
a_longer_name = "hello, CFG!"
print (age)
print (a_longer_name)
age=5
age="almost there"
age=29.5
age="I really don't know!"
print(age)

"""task 3 """

print("hello" + "world")
print("joke" *3)
print("chen"+ str(3))
print("hello".upper())
print("GOODBYE".lower())
print("the lord of the rings".title())


s1="hello" + "world"
s2="joke"*3
s3=5
print(s1 + " " + s2*10)
print(s1 + " " + s2 + " " +  " " + str(s3))

strExample="a,b,b,s,happy"
print(strExample.split(","))

"""string formatting"""
age=6
like="painting"

age_description="My age is {} and I like {}.".format(age,like)
print(age_description)

age_description2="My age is {0} and I like {1}.".format(age,like)
print(age_description2)
"""here the variables are pivate, if we change the age 
variable below, age_description variables will not change.
the code is read sequentially. Everything is provate, inside a scope.
NOT GLOBAL
Question: is this the case in Javascript? 
ANSWER: Yes this is exactly the same in JS"""

rabbit="""bugs bunny

is a cool rabit"""
print(rabbit)

"""homework end of chapetr 2"""

print(10/3)
print(10%3)

a=1
a=a+1
a = 1
a = a + 1 
print (a)
b = "hello" 
print (b)
c = b.title() 
print (b)
print (c)
d = "hello"
e = d.title()
print (d)
print (e)
name = "Dave"
f = "Hello {0}! ".format(name) 
print (f)
name = "Sarah"
print (f)
print (f *5)
















