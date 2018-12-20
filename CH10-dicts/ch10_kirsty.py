#------------------------------------------------------------------------------
#                    CHAPTER 10: DICTIONARIES
#------------------------------------------------------------------------------


#---------------------TASK 1: CREATE DICTIONARY--------------------------------
tel = {"alf":1111111111, "bobby": 1424732210, "Bill": 1432710276}
print(tel)
#--------------TASK 2: ASSIGN, RETRIEVE, UPDATE VALUES------------

#UPDATE ALF KEYS VALUE.
tel["alf"]=123445
print(tel["alf"])

#ASSIGN NEW KEY FRED WITH VALUE.
tel["Fred"] = "01424"
print(tel)

#ASSIGN NEW KEY WHICH IS A TUPLE CONTAINING STRINGS.
tilly = "Tilly"
joke = "007"
tel[(joke, tilly)] = "the keY is a tuple"
print(tel)


EVE,
#--------------TASK 3: LOOK UP AND DELETE VALUES-------------------------------

#REMOVE KEY VALUE PAIRS
del tel["bobby"]
print(tel)

#--------------------TASK 4: RETRIEVE KEYS AND VALUES FROM DICT---------------------
#ACCESS KEYS OR VALUES FROM DICT
x = tel.keys()
print(x)
y = tel.values()
print(y)
print(type(x))


#-------------TASK 5: CONVERT KEYS AND VALUES TO LIST DATA TYPE---------------------------------
"""
DICTIONARIES ARE UNORERED,SO DON'T SUPPORT INDEXING. 
IF WE WANT TO OBTAIN THE FIRST KEY IN THE DICTIONARY, WE MUST CONVERT TO LIST TYPE FIRST.

"""
PRINT(list(tel.keys())[0]) 

print(list(tel.keys()))
y = tel.values()
print(type(y))
print(y)
print(list(tel.values()))
print(list(y)[0])


#--------------------------TASK 6: AVOID KEY ERRORS--------------------


"""
    WE CAN CHECK THAT A KEY IS PRESENT IN A DICT USING AN IF ELSE STATEMENT AS BELOW.
"""
k = ’eric’
if k in tel: 
    print(k, ’:’, tel[k]) 
else: 
    print(k, ’not found!’)

#MORE EXAMPLES

    if "alf" in tel:
    print("alf", ":", tel["alf"])
else:
    print("alf", "not found")


if "mike" in tel:
    print("mike", ":", tel["mike"])
else:
    print("mike", "not found")


#--------------------------TASK 7 & 8: SORTING A DICTIONARY--------------------

    
#--------------------------SORTING KEYS---------------------------------------------------
    
people_age = {"chloe": [13, 6], "alice": [29, 9], "sarah": [3, 2], "Mike": [1,8], "katie": [53, 4]}

labels = list(people_age.keys())

#SORT LABELS (LIST OF KEYS) BY KEY VALUES, VALUE WITH INDEX 1.
labels.sort(key = lambda k: people_age[k][1])
print(labels)

#--------------------------SORTING KEY VALUE PAIRS---------------------------------------------------
people_age = {"chloe": [13, 6, "a"], "alice": [29, 9, "b"], "sarah": [3, 2, "c"], "Mike": [1,8, "d"], "katie": [53, 4, "e"]}
labels = list(people_age.keys())
#NOW SORTING KEY VALUE PAIRS. THE DICT IS RETURNED AS TUPLES WITH KEY POSITION 0 AND VALUE POSITION 1.
x = sorted(people_age.items(), key = lambda kv: kv[1])
print("x is sorted by the value index 1 " + str(x))

#HERE WE ARE SORTING BY VALUES, VALUE IN 1ST INDEX.
print(sorted(people_age.items(), key = lambda kv:kv[1][1]))

sorted(people_age.items(), key = lambda kv:kv[1], reverse=True)

#-------------create and sort metal dictionary------------------------------
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



















