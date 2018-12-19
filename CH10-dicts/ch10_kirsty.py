# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 10:06:29 2018

@author: Gebruiker
"""
#---------------------TASK 1: CREATE DICTIONARY--------------------------------
tel = {"alf":1111111111, "bobby": 1424732210, "Bill": 1432710276}
tel["alf"]=123445
print(tel)
tel["Fred"] = "01424"
print(tel)
print(tel["alf"])
#--------------TASK 2,3+4: ASSIGN, RETRIEVE, DELETE & UPDATE VALUES------------
tilly = "Tilly"
joke = "007"
tel[(joke, tilly)] = "the keY is a tuple"
print(tel)

del tel["bobby"]
print(tel)
x = tel.keys()
print(type(x))
print(x)
#-------------TASK5 -CONVERT TO LIST DATA TYPE---------------------------------
print(list(tel.keys()))
y = tel.values()
print(type(y))
print(y)
print(list(tel.values()))

print(list(y)[0])

if "alf" in tel:
    print("alf", ":", tel["alf"])
else:
    print("alf", "not found")


if "mike" in tel:
    print("mike", ":", tel["mike"])
else:
    print("mike", "not found")
    
bill = {'a':3, 'c':1, 'b':5}
labels = list(bill.keys())
print(labels)
labels.sort(key=lambda k:bill[k])
print(labels)
bill['g'] = 8
bill['f']=10
bill['o']=20
print(bill)
labels = list(bill.keys())
print(labels)
labels.sort(key=lambda k:bill[k])
print(labels)

#--------------------------TASK 7 & 8: SORTING A DICTIONARY--------------------
people_age = {"chloe": [13, 6], "alice": [29, 9], "sarah": [3, 2], "Mike": [1,8], "katie": [53, 4]}
labels = list(people_age.keys())
labels.sort(key = lambda k: people_age[k][1])
print(labels)
print(labels[::-1])

people_age = {"chloe": [13, 6, "a"], "alice": [29, 9, "b"], "sarah": [3, 2, "c"], "Mike": [1,8, "d"], "katie": [53, 4, "e"]}

labels = list(people_age.keys())

x = sorted(people_age.items(), key = lambda kv: kv[1])
print("x is sorted by the value index 1 " + str(x))

#print(labels)
#print(labels[::-1])


print(sorted(people_age.items(), key = lambda kv:kv[1][1]))

sorted(people_age.items(), key = lambda kv:kv[1], reverse=True)

#-------------create and sorting metal dictionary------------------------------
metal = {"Barium": [3594, 1000, 56 ], "Aluminum": [2712, 933, 13], "Chromium": [7190, 2180, 24], "Cobalt":[8746, 1768, 27 ], "Copper":[8940, 1358, 29 ] }
"""sort by density in kg/m^3"""
print("Sorted by density: " + str(sorted(metal.items(), key = lambda kv:kv[1][0])))
print("Sorted by density: " + str(sorted(metal, key = lambda k:metal[k])))
print("top three(least dense): " + (str(sorted(metal.items(), key = lambda kv:kv[1][0])[0:3])))
print("top three(most dense): " + (str(sorted(metal.items(), reverse = True, key = lambda kv:kv[1][0])[0:3])))


"""sort by m.p. in kelvin"""
print("Sorted by melting point: " + str(sorted(metal.items(), key = lambda kv:kv[1][1])))
print("sorted by melting point: " + str(sorted(metal, key = lambda k:metal[k][1])))
print("top three(lowest m.p.): " + (str(sorted(metal.items(), key = lambda kv:kv[1][1])[0:3])))
print("top three(highest m.p.): " + (str(sorted(metal.items(), reverse = True, key = lambda kv:kv[1][1])[0:3])))

"""sort by atomic numebr"""
print("Sorted by atomic number: " + str(sorted(metal.items(), key = lambda kv:kv[1][2])))
print("Sorted by atomic number: " + str(sorted(metal, key = lambda k:metal[k][2])))
print("top three(lowest atomic number): " + (str(sorted(metal.items(), key = lambda kv:kv[1][2])[0:3])))
print()
print("top three(highest atomic number): " + (str(sorted(metal.items(), reverse = True, key = lambda kv:kv[1][2])[0:3])))



















