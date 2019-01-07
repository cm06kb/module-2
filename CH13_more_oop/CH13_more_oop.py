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


p1 = Person("John", 44, "m")
p1.name
p1.isMale

#----------------------7.2 - MORE FUNCTIONALITIES FOR THE PERSON CLASS----------------------