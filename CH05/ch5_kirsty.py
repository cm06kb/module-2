# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 10:07:55 2018

@author: Gebruiker
"""

class Customer(object): 
    def __init__(self, name, balance=0.0):       
        """Return a Customer object whose name is *name* and starting  
        balance is *balance*."""        
        self.name = name        
        self.balance = balance
 
    def withdraw(self, amount):       
        """Return the balance remaining after withdrawing *amount* dollars."""        
        if amount > self.balance:            
            raise RuntimeError('Amount greater than available balance.')
        self.balance -= amount        
        return self.balance

    def deposit(self, amount):       
        """Return the balance remaining after depositing *amount* dollars."""        
        self.balance += amount        
        return self.balance

jason = Customer("Jason Taylor", 1000.0)
print(jason.balance)
print(jason.name)
jason.withdraw(200)
print(jason.balance)


class Animal(): 
    def eat(self): 
        print("yum") 
class Dog(Animal): 
    def bark(self):
        print("Woof!") 
class GreyHound(Dog):
    def hobby(self):
        print("racing")
class Cat(Animal): 
    def meow(self): 
        print("Meow")
Snoopy = Dog()
Snoopy.bark()
Snoopy.eat()
jack = GreyHound()
jack.hobby()
jack.eat()
 
class Robot():
    def move(self):
        print("...move move move...")

class CleanRobot(Robot):
    def clean(self):
        print("I vaccum dust")

class CookRobot(Robot):
    def cook(self):
        print("I make rice")


maid= CleanRobot()
maid.clean()

chef = CookRobot()
chef.cook()


