# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 10:07:55 2018

@author: Gebruiker
"""
import sys

#class Customer(object): 
#    def __init__(self, name, balance=0.0):       
#        """Return a Customer object whose name is *name* and starting  
#        balance is *balance*."""        
#        self.name = name        
#        self.balance = balance
# 
#    def withdraw(self, amount):       
#        """Return the balance remaining after withdrawing *amount* dollars."""        
#        if amount > self.balance:            
#            raise RuntimeError('Amount greater than available balance.')
#        self.balance -= amount        
#        return self.balance
#
#    def deposit(self, amount):       
#        """Return the balance remaining after depositing *amount* dollars."""        
#        self.balance += amount        
#        return self.balance
#
#jason = Customer("Jason Taylor", 1000.0)
#print(jason.balance)
#print(jason.name)
#jason.withdraw(200)
#print(jason.balance)
#
#
#class Animal(): 
#    def eat(self): 
#        print("yum") 
#class Dog(Animal): 
#    def bark(self):
#        print("Woof!") 
#    def detect(self):
#        if self.barkNumber>=3:
#            print('strenger coming!!!')
#    def cat(self):
#        if self.
#class GreyHound(Dog):
#    def hobby(self):
#        print("racing")
#class Cat(Animal): 
#    def meow(self): 
#        print("Meow")
#Snoopy = Dog()
#Snoopy.bark()
#Snoopy.eat()
#jack = GreyHound()
#jack.hobby()
#jack.eat()
# 
#class Robot():
#    def move(self):
#        print("...move move move...")
#
#class CleanRobot(Robot):
#    def clean(self):
#        print("I vaccum dust")
#
#class CookRobot(Robot):
#    def cook(self):
#        print("I make rice")
#
#
#maid= CleanRobot()
#maid.clean()
#
#chef = CookRobot()
#chef.cook()

#class Animal():
#    def __init__(self, name, age=0):
#        self.name = name
#        
#    def eat(self):
#         print('yum')
#         
#class Dog(Animal):
#    def __init__(self, name, age=0,barkNumber=0):
#        self.barkNumber = barkNumber
#        
#    def bark(self):
#        print('Woof! '*self.barkNumber)
#        
#        
#class DogAgent(Dog):
#    def detect(self):
#        if self.barkNumber>=3:
#            print('stranger coming!!!')
#        
#class Cat(Animal):
#    def meow(self):
#        print('Meow')
#name = input('what is your pet\'s name:')        
#age = int(input('what is your pet\'s age: '))
#bark = int(input('how many times you heard it barked: '))
#
#dog007 = DogAgent(name, age, bark) #always inheritant ancester's
#dog007.bark()
#dog007.eat()
#dog007.detect()


"""Okay now my own example"""


#class School_members():
#    def __init__(self, name, gender, age=0):
#        self.name = name
#        self.gender = gender
#    def lunch_time(self):
#        print("yey, lunch time!")
#        
#class Pupil(School_members):
#    def __init__(self, name, gender, age=0, favourite_subject=''):
#        self.favourite_subject = favourite_subject
#    def response_to_fav_subject(self):
#        if self.favourite_subject == "math":
#            print("Math is your favourite subject?! What a nerd...")
#        elif self.favourite_subject == "french":
#            print("Bonjour...")
#        elif self.favourite_subject == "science":
#            print("sure it is...")
#        else:
#            print("whatever...")
#
#class Teacher(School_members):
#    def __init__(self, name, gender, age=0, how_many_subject_they_teach=0):
#        self.how_many_subject_they_teach=how_many_subject_they_teach
#    def response_to_how_many_sub_they_teach(self):
#        pay = 25
#        salary = pay * how_many_subject_they_teach
#        return "As you teach {} subjects, you will earn £{}".format(pay, salary)
#            
#class Science_depart(Teacher):
#    def __init__(self, name, gender, age=0, how_many_subject_they_teach=0, have_you_turned_gas_off = ""):
#        self.have_you_turned_gas_off = have_you_turned_gas_off
#    
#    def response_to_gas(self):
#        if have_you_turned_gas_off == "y":
#            return "Well done"
#        if have_you_turned_gas_off == "n":
#            return "Okay, I think I know what caused the fire...."
#        
#
#        
#name = input("what is your name? ")
#age = int(input("what is your age? "))
#gender = input("Are you male or female?  ")
#favourite_subject = input("what is your favourite subject?  ")
#how_many_subject_they_teach = int(input("How many subject do you teach?"))
#have_you_turned_gas_off = input("did you turn the gas off in the lab? ")
#
#
#bill = Pupil(name, gender, age, favourite_subject)
#print(bill.response_to_fav_subject())
#
#mr_smith = Teacher(name, gender, age, how_many_subject_they_teach)
#print(mr_smith.response_to_how_many_sub_they_teach())
#
#mr_nye = Science_depart(name, gender, age, how_many_subject_they_teach, have_you_turned_gas_off)
#print(mr_nye.response_to_gas())



"""using composition to link rather than inheritance"""

class Animal():
#   def __init__(self, name, age):
#       self.name = name
#       self.age = age
   def eat(self):
         print('yum')

class Dog(Animal):
    def bark(self):
        print("Woof!") 
        
    def detect(self):
        if self.barkNumber>=3:
            print('stranger coming!!!')

class Robot():
    def move(self):
        print("...move move move...")
        
    def move2(self):
        print("..eer twist")

class CleanRobot(Robot):
    def clean(self):
        print("I vaccum dust")



class SuperRobot(): 
    def __init__(self, name, age): 
        
        self.name = name
        self.age = age
        self.ted = Robot() 
        self.o2= Dog() 
        self.o3 = CleanRobot() 
    def show_name_and_age(self):
        print(name)
        print(age)
 
    def what_should_i_do(self): 
        ask_user = input("Hi, my name is {}, what would you like me to do?".format(self.name))
        if ask_user=="clean":
            return self.clean()  
        else:
            return self.playGame()
    def playGame(self): 
        print("alphago game") 
        
    def move(self): 
        return self.ted.move() 
    
    def bark(self): 
        return self.o2.bark()
    
    def clean(self): 
        return self.o3.clean()

name =  sys.argv[1]
age = sys.argv[2]


hal = SuperRobot(name, age)
hal.show_name_and_age()
hal.what_should_i_do()
#bill.what_should_i_do()






