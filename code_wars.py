# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 14:02:00 2018

@author: Gebruiker
"""


#def make_password(phrase):
#        phrase_list = phrase.split(" ")
#        password = []
#        for n in phrase_list:
#            if n[0] == "o" or n[0] == "O":
#                password.append("0")
#            elif n[0] == "i" or n[0] == "I":
#                password.append("1")
#            elif n[0] == "s" or  n[0] == "S":
#                password.append("5")
#            else:    
#                password.append(n[0])
#        
#        password = "".join(password)
#        return password
#            
#print(make_password("Should Work for ome examples"))

#def starter(hive):
#    count = 0
#    runs = 0
#    return how_many_bees(hive, count, runs)
#
#def how_many_bees(hive, count, runs):
#    count = count
#    runs = runs
#    if runs == 0:
#        n=0
#        m = 0
#        scan_row(hive, n, m, count, runs)
#    if runs == 1:
#        n=1
#        m = 0
#        scan_row(hive, n, m, count, runs) 
#    if runs == 3:
#        n=2
#        m = 0
#        scan_row(hive, n, m, count, runs)   
#    else:
#        answer = count
#        return answer    
#    return answer
#
#
#def scan_row(hive, n, m, count, runs):    
#    while m<7:
#        if (hive[n][m]=="b" and hive[n][m+1] == "e" and hive[n][m+2] =="e") or (hive[n][m]=="e" and hive[n][m+1] == "e" and hive[n][m+2] =="b"):
#            count = count + 1
#            m = m + 4
#        else:
#            m = m + 4
#    runs = runs + 1
#    return how_many_bees(hive, count, runs)




#def how_many_bees(hive):
#    if (not hive) or (len(hive) < 0):
#        return 0
#    else:
#        new_hive = vertical_hive(hive)
#        total_h = scan_row(hive)
#        total_v = counting_rows(new_hive)
#        total = total_h + total_v
#        return total
# 
#def vertical_hive(hive):
#    r = 0
#    new_hive = []
#    for char in hive[0]:
#        if r < len(hive[0]):
#            new_row = ''
#            for i in range(0, len(hive)):
#                new_row += hive[i][r]
#        new_hive.append(new_row)
#        r = r + 1
#    return new_hive
#
#def counting_rows(hive):
#    bees = 0
#    for row in hive:
#        i = 0
#        for char in row:
#            if (row[i:i+3] == 'bee') or (row[i:i+3] == 'eeb'):
#                #if (row[i:i+3] == 'bee'): print(row, i, row[i:i+3])
#                #if (row[i:i+3] == 'eeb'): print(row, i, row[i:i+3])
#                bees = bees + 1
#            i = i + 1
#    return bees
#
#def scan_row(hive):
#   row = 0
#   no_of_columns = (len(hive[0])-1)
#   no_of_rows = (len(hive)-1)
#   total_num_bee_in_rows = 0
#   while row<=(no_of_rows):
#       column = 0
#       while column+2<=(no_of_columns):
#           if (hive[row][column]=="b" and hive[row][column+1] == "e" and hive[row][column+2] =="e") or (hive[row][column]=="e" and hive[row][column+1] == "e" and hive[row][column+2] =="b"):
#               total_num_bee_in_rows = total_num_bee_in_rows + 1
#               column = column + 1
#           else:
#              column = column + 1
#       row = row + 1
#   return total_num_bee_in_rows


#def capitalize(s):
#    ans = []
#    for i in range(len(s)):
#        if i%2 == 0:
#            ans.append(s[i].upper())
#        else:
#            ans.append(s[i])
#    ans = "".join(ans)
#    for i in range(len(s)):
#        if i%2 != 0:
#            ans.append(s[i].upper())
#        else:
#            ans.append(s[i])
#    
#    return ans
#
#print(capitalize("codewars"),['CoDeWaRs', 'cOdEwArS'])

import itertools

  
def smallest(n):
    
#    poss_perms = list(map("".join, itertools.permutations(str(n))))
    
    n = str(n)   
    list_int = []
    for i in n:
        list_int.append(int(i))
        
    b = sorted(list_int)
    ans =[]
    count = 0
    num_of_interest = "x"
    original_num =  "q"
    for x in range(len(list_int)):
            if list_int[x] != b[0] and count == 0:
                    num_of_interest = list_int[x]
                    original_num = b[0]
                    ans.append(b[0])
                    count += 1
#                   new = "".join(str(list_int))
                    i = b.index(b[x])
                    j = list_int.index(b[x])
            
            else:
                ans.append(list_int[x])
                
            
    str1 = ''.join(str(e) for e in ans)
    str1 = int(str1)
    str1.split
    final = [n, str1, j, i] 
    return final

#    list_int = []
#    for i in poss_perms:
#        list_int.append(int(i))
#    list_int.sort()
    
#    new = str(list_int[0])
#       
#    for x in range(len(old)-1):
#            if old[x] != new[x]:
#                if new[x] < old[x]:
#                    i = old.find(new[x])
#                    j = new.index(new[x])
#                    return new, i, j
#            else:
#                pass

print(smallest(269045))

#print(smallest(261235))
#print(smallest(209917))
#
#print(smallest(285365))













