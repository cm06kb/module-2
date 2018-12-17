# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 10:06:29 2018

@author: Gebruiker
"""

#tel = {"alf":1111111111, "bobby": 1424732210, "Bill": 1432710276}
#tel["alf"]=123445
#print(tel)
#tel["Fred"] = "01424"
#print(tel)
#print(tel["alf"])
#tilly = "Tilly"
#joke = "007"
#tel[(joke, tilly)] = "the ket is a tuple"
#print(tel)
#del tel["bobby"]
#print(tel)
#x = tel.keys()
#print(type(x))
#print(x)
#print(list(tel.keys()))
#y = tel.values()
#print(type(y))
#print(y)
#print(list(tel.values()))
#
#print(list(y)[0])
#
#if "alf" in tel:
#    print("alf", ":", tel["alf"])
#else:
#    print("alf", "not found")
#
#
#if "mike" in tel:
#    print("mike", ":", tel["mike"])
#else:
#    print("mike", "not found")
    
#bill = {'a':3, 'c':1, 'b':5}
#labels = list(bill.keys())
#print(labels)
#labels.sort(key=lambda k:bill[k])
#print(labels)
#bill['g'] = 8
#bill['f']=10
#bill['o']=20
#print(bill)
#labels = list(bill.keys())
#print(labels)
#labels.sort(key=lambda k:bill[k])
#print(labels)


#people_age = {"chloe": [13, 6], "alice": [29, 9], "sarah": [3, 2], "Mike": [1,8], "katie": [53, 4]}
#labels = list(people_age.keys())
#labels.sort(key = lambda k: people_age[k][1])
#print(labels)
#print(labels[::-1])

#people_age = {"chloe": [13, 6, "a"], "alice": [29, 9, "b"], "sarah": [3, 2, "c"], "Mike": [1,8, "d"], "katie": [53, 4, "e"]}
#
#labels = list(people_age.keys())
#
#x = sorted(people_age.items(), key = lambda kv: kv[1])
#print("x is sorted by the value index 1 " + str(x))
#
##print(labels)
##print(labels[::-1])


#print(sorted(people_age.items(), key = lambda kv:kv[1][1]))

#sorted(people_age.items(), key = lambda kv:kv[1], reverse=True)


#metal = {"Barium": [3594, 1000, 56 ], "Aluminum": [2712, 933, 13], "Chromium": [7190, 2180, 24], "Cobalt":[8746, 1768, 27 ], "Copper":[8940, 1358, 29 ] }
#"""sort by density in kg/m^3"""
#print("Sorted by density: " + str(sorted(metal.items(), key = lambda kv:kv[1][0])))
#print("Sorted by density: " + str(sorted(metal, key = lambda k:metal[k])))
#print("top three(least dense): " + (str(sorted(metal.items(), key = lambda kv:kv[1][0])[0:3])))
#print("top three(most dense): " + (str(sorted(metal.items(), reverse = True, key = lambda kv:kv[1][0])[0:3])))
#
#
#"""sort by m.p. in kelvin"""
#print("Sorted by melting point: " + str(sorted(metal.items(), key = lambda kv:kv[1][1])))
#print("sorted by melting point: " + str(sorted(metal, key = lambda k:metal[k][1])))
#print("top three(lowest m.p.): " + (str(sorted(metal.items(), key = lambda kv:kv[1][1])[0:3])))
#print("top three(highest m.p.): " + (str(sorted(metal.items(), reverse = True, key = lambda kv:kv[1][1])[0:3])))
#
#"""sort by atomic numebr"""
#print("Sorted by atomic number: " + str(sorted(metal.items(), key = lambda kv:kv[1][2])))
#print("Sorted by atomic number: " + str(sorted(metal, key = lambda k:metal[k][2])))
#print("top three(lowest atomic number): " + (str(sorted(metal.items(), key = lambda kv:kv[1][2])[0:3])))
#print()
#print("top three(highest atomic number): " + (str(sorted(metal.items(), reverse = True, key = lambda kv:kv[1][2])[0:3])))



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


















