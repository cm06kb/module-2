# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 12:05:20 2018

@author: Gebruiker
"""

-----------------------------CREATE OWN DICT TO SORT WITHIN CLASS-----------------------

"""write a function that can generate a phonebook_dict containing four keys, each 
key should have four values. Obtain values via user input."""
#class Classmate():
#    def __init__(self, name, phone, lucky, postcode, town):
#        self.name = name
#        self.phone = phone
#        self.lucky = lucky
#        self.postcode = postcode
#        self.town = town 
#    
#    def add_dets_to_dict(self,class_details):
#        class_details[self.name] = [self.phone, self.lucky, self.postcode, self.town]
#        return self.queen_age_comparison(class_details)
#    def queen_age_comparison(self, class_details):    
#        age = int(input("Oh also what is your age? :"))
#        if age<92:
#            diff_in_age = 92 - age
#            print("Did you know you are {} years younger than the Queen".format(diff_in_age))
#            class_details[self.name].append(diff_in_age)
#        elif age>92:
#            diff_in_age = age - 92
#            print("Did you know you are {} years older than the Queen".format(diff_in_age))
#            class_details[self.name].append(diff_in_age)
#        elif 92 == age:
#            print("Hey your the same age as the Queen") 
#            class_details[self.name].append(diff_in_age)
#        else:
#            print("hmm something not quite right, let's try that again")
#            return self.queen_age_comparison(class_details)
#        again = input("would you like to add another student? type Y/N: ")
#        if again == "Y":
#            return add_a_student(class_details)
#        else:
#            return self.sorting_options(class_details)
#            
#    def sorting_options(self, class_details):
#        sorting_alpha = input("type 1 to sort by name, type 2 to sort by town, type 3 to sort by lucky number, type 4 to sort by difference in your age and the queens: " )
#        if sorting_alpha == "1":
#            return self.sort_name(class_details)
#        elif sorting_alpha == "2":
#            return self.sort_town(class_details)
#        elif sorting_alpha == "3":
#            return self.sort_luckynum(class_details)
#        elif sorting_alpha == "4":
#            return self.sort_queen(class_details)
#        else:
#            print("hmm, thats not right. Try again")
#            return self.sorting_options(class_details)
#    
#    def sort_name(self, class_details):
#        rearranged = sorted(class_details.items(), key = lambda kv:kv[0])
#        print(rearranged)
#    
#    def sort_town(self, class_details):
#        rearranged = sorted(class_details.items(), key = lambda kv:kv[1][3])
#        print(rearranged)
#    
#    def sort_luckynum(self, class_details):
#        rearranged = sorted(class_details.items(), key = lambda kv:kv[1][1])
#        print(rearranged)
#    
#    def sort_queen(self, class_details):
#        rearranged = sorted(class_details.items(), key = lambda kv:kv[1][4])
#        print(rearranged)
#
#def add_a_student(class_details):
#    name = input("Please enter your name: " )
#    name = name.lower()    
#    student = name[0].upper()  + name[1::] 
#    phone = input("Please enter the last three digits of your phone number: " )
#    lucky = input("Please enter your lucky number: " )
#    postcode = input("Please enter your postcode: " )
#    town = input("Please enter your town/city: " )
#    student = Classmate(name, phone, lucky, postcode, town)
#    return student.add_dets_to_dict(class_details)
#
#
#class_details = {}
#add_a_student(class_details)


class Classmate():
    def __init__(self, name, phone, lucky, postcode, town):
        self.name = name
        self.phone = phone
        self.lucky = lucky
        self.postcode = postcode
        self.town = town 
    
    def add_dets_to_dict(self,class_details):
        class_details[self.name] = [self.phone, self.lucky, self.postcode, self.town]
        return self.queen_age_comparison(class_details)
    
    def queen_age_comparison(self, class_details):    
        age = int(input("Oh also what is your age? :"))
        if age<92:
            diff_in_age = 92 - age
            print("Did you know you are {} years younger than the Queen".format(diff_in_age))
            class_details[self.name].append(diff_in_age)
        elif age>92:
            diff_in_age = age - 92
            print("Did you know you are {} years older than the Queen".format(diff_in_age))
            class_details[self.name].append(diff_in_age)
        elif 92 == age:
            print("Hey your the same age as the Queen") 
            class_details[self.name].append(diff_in_age)
        else:
            print("hmm something not quite right, let's try that again")
            return self.queen_age_comparison(class_details)
        
        again = input("would you like to add another student? type Y/N: ")
        again = again.lower()
        if again == "y" or again =="yes":
            return add_a_student(class_details)
        else:
            return self.sorting_options(class_details)
            
    def sorting_options(self, class_details):
        sorting_alpha = input("type 1 to sort by name, type 2 to sort by town, type 3 to sort by lucky number, type 4 to sort by difference in your age and the queens: " )
        if sorting_alpha == "1":
            return self.sort_name(class_details)
        elif sorting_alpha == "2":
            return self.sort_town(class_details)
        elif sorting_alpha == "3":
            return self.sort_luckynum(class_details)
        elif sorting_alpha == "4":
            return self.sort_queen(class_details)
        else:
            print("hmm, thats not right. Try again")
            return self.sorting_options(class_details)
    
    def sort_name(self, class_details):
        rearranged = sorted(class_details.items(), key = lambda kv:kv[0])
        print(rearranged)
    
    def sort_town(self, class_details):
        rearranged = sorted(class_details.items(), key = lambda kv:kv[1][3])
        print(rearranged)
    
    def sort_luckynum(self, class_details):
        rearranged = sorted(class_details.items(), key = lambda kv:kv[1][1])
        print(rearranged)
    
    def sort_queen(self, class_details):
        rearranged = sorted(class_details.items(), key = lambda kv:kv[1][4])
        print(rearranged)

       
def add_a_student(class_details):
    name = input("Please enter your name: " )
    name = name.lower()    
    student = name[0].upper()  + name[1::] 
    phone = get_phone_num()
    lucky = input("Please enter your lucky number: " )
    postcode = input("Please enter your postcode: " )
    town = input("Please enter your town/city: " )
    student = Classmate(name, phone, lucky, postcode, town)
    return student.add_dets_to_dict(class_details)

def get_phone_num():
    phone = input("Please enter the last three digits of your phone number: " )
    if len(phone) == 3:
        return phone
    else:
        print("Hmm, thats not right, try again.")
        return get_phone_num()

class_details = {}
add_a_student(class_details)
