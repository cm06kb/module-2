#------------------------------------------------------------------------------
#                   CHAPTER 13 - MORE OOP
#------------------------------------------------------------------------------

#----------------------7.1 - INITIALISE  THE PERSON CLASS----------------------

class Person:
    """
        created a class person, whcih has variables name, age and gender
        initialisation method created, whihc is called when an instance of class person is created.
        
        
    """
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        if gender == "m":
            self.isMale = True
        elif gender == "f":
            self.isMale = False
        else:
            print("Gender not recognised!")
#add method for task 7.2 - greeting methods
    def greetingInformal(self):
        print("Hi", self.name)
        
    def greetingFormal(self):
        if self.isMale:
            print("Welcome, Mr ", self.name)
        else:
            print("Welcome, Ms ", self.name)

#add method for task 7.3 - greeting filter method
    def greetingAgeBased(self):
        if self.age < 18:
            print("Welcome, yound ", self.name)
        elif self.age > 60:
            print("Welcome, venerable ", self.name)
        else:
            self.greetingFormal()
            
p1 = Person("John", 44, "m")
p1.name
p1.isMale

#----------------------7.2 - MORE FUNCTIONALITIES FOR THE PERSON CLASS----------------------

p1 = Person("Harry", 12, "m" )
p2 = Person("Jean", 12, "m")
p1.greetingInformal()
p2.greetingFormal()

#----------------------7.3 - GREETING FILTER------------------------------------

p3 = Person("Richard", 50, "m")
p2.greetingAgeBased()
p3.greetingAgeBased()

#----------------------7.4 - SUBCLASS FOR THE PERSON CLASS----------------------


class Wizard(Person):
    """
        subclass of parent class
    """
    
    def greetingFormal(self):
        print("Welcome, Mr ", self.name, end = " ")
        print("- you're a fine wizard!")

p1 = Wizard("Harry", 12, "m")
p1.greetingFormal()
    
    
#----------------------7.5 - REDEFINE INIT-------------------------------------

# Subclasses can inherit the init method of the parent class but we can chose
# to overwrite it.

class Witch(Person):
    """
        the init method below envokes parent class Person
    """
    
    def __init__ (self, name, age , gender):
        Person.__init__(self, name, age, "f")
    
    def greetingFormal(self):
        print("Welcome, Ms ", self.name, end = " ")
        print("- you're a fine Witch!")

p1 = Witch("Hermoine", 12, "f")
p1.greetingFormal()
        
#----------------------7.6 -ADD METHODS TO SUBCLASS-------------------------------------

# Subclasses can have their wn methods which the parent class cannot use.

class Giant(Person):
    """
        the init method below envokes parent class Person
    """
    
    def __init__ (self, name, age , gender):
        Person.__init__(self, name, age, "m")
    
    def greetingFormal(self):
        print("Welcome, Mr ", self.name, end = " ")
        print("- you're a fine Giant!")

    def spell(self):
        print("Expelliarmus!")

p1 = Giant("Hagrid", 55, "m")
p1.greetingFormal()
p1.spell()




















