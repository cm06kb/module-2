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




def how_many_bees(hive):
    if hive==None:
        return 0
    else:
        total_no_of_bees_in_column = scan_column(hive)
        total_num_bee_in_rows = scan_row(hive)
        return total_num_bee_in_rows + total_no_of_bees_in_column
""" n is the row"""
""" m is the column"""
"""len(hive)-1 is the column height"""
"""len(hive[0])-1 is the row length"""

def scan_column(hive):

    column = 0
    no_of_rows = (len(hive))
    no_of_columns= (len(hive[0])-1) 
    total_no_of_bees_in_column = 0
#    while column<=((no_of_columns)):
#        row = 0
#        print(no_of_rows)
#        while row+2<=(no_of_rows):
#            print(row)
#            if ((hive[row:row+3][column] == "bee") or (hive[row:row+3][column] == "eeb")) and (row<no_of_rows-3):
#                 
##            if (hive[row][column]=="b" and hive[row+1][column] == "e" and hive[row+2][column] =="e") or (hive[row][column]=="e" and hive[row+1][column] == "e" and hive[row+2][column] =="b"):
#                total_no_of_bees_in_column = total_no_of_bees_in_column + 1
#                row = row + 1
#            else:
#                row = row + 1
#        column = column + 1
    return number_of_bees 


def scan_row(hive):
    row = 0
    no_of_columns = (len(hive[0])-1)
    no_of_rows = (len(hive)) 
    total_num_bee_in_rows = 0
#    while row<=(no_of_rows):
#        column = 0
#        while column+2<=(no_of_columns):
##            print(hive[row][column:column+3])
##            if (hive[row][column:column+3] == "bee") or (hive[row][column:column+3] =="eeb"):
#                
#            if (hive[row][column]=="b" and hive[row][column+1] == "e" and hive[row][column+2] =="e") or (hive[row][column]=="e" and hive[row][column+1] == "e" and hive[row][column+2] =="b"):
#                total_num_bee_in_rows = total_num_bee_in_rows + 1
#                column = column + 1
#            else:
#               column = column + 1
#        row = row + 1
    return total_num_bee_in_rows     

#print(how_many_bees([".b.e.ebebbee..ee.e", "b.ee.b.e.eebbee.e.", "e.bb.ee..eee.ebeb.", "eb.eee.beb.e..ebe.", "eee.eb..b.ebe..bee", ".ebe.ee.be.beee.b.", "bebb..eeeee..b.ee.", "..ee.eee.eb.ebbbe.", "eebeebe.e.b.ee...b", "ebee.eebbe...e..eb", "bee..e...bbeeeeb.e", "ee.bbeeeb..e..e.eb", "be.bee....eebeebe.", ".bee.eebbeebe...e.", "ee.ebe.b.eebee..b.", "eebeebebb.e..ee...", "eeb.eb.e.e..e.ebbe", "eb.e..eb.eeeebb..e"]))
print(how_many_bees(["bee.bee", ".e..e..",".b..eeb"]))
#print(how_many_bees(["beebee", "ee.e.e","eb.eeb"]))


"""column m is equal to row n"""
#bee.bee
#.e..e..
#.b..eeb

"""column m is less than row n, more rows than columns......"""

#bebe..bee.e..beb.ee..be.eee
#.bee.ee.ee.e..ee.bb.ee.ebbb
#.b.e.b.ee.eeeeee..ebb.eb.be
#..eee.b.b.ee..bebbeee.eb.ee
#..ee..be...ebbeebe.eebeeeb.
#eebeb..e.eeee.b.eb.b..ee.be
#bebebe..eee.e..e...e.bbeebe
#beee..eebeebbe.b.eeb...ee..
#.e.be.ebbbee.eee....eeb.bee
#bbeeeeeee.e.eb...b...ebee.b
#eee.e.e.eebe.bbe.be.e.bb.e.
#ebee..ebb.ee..ebe..eeb..eeb
#bbeeeeeb....ee.ebbe...eeeb.
#beee.e...ee.b.eb.eeeeeb.bb.
#e.eebbe.eeb.e.b..e..eeebbe.
#ebeee.beeeee..e..ebb..b.be.
#eeb.e.ebe.eb..be..e.e.eebeb
#beee.bbb..ebe...ee.beee.ee.
#bebeb..ee.bb.ee....b.eeeeee
#b.ee....eebb.ebebeb.eee..ee
#e.eb.be.bee.ebee.e.b.e.eeb.
#.e..eebb.ee.b..bee.eeb.beee
#eeee..e.b.ee.ebb..ebe.be.be
#.e.b.bb..eee.be.eeebe.eebe.
#ee..bebe.ee.b..eeeb.beebe..
#b.e.e.ee..ee.eebeb.b.ebbe.e
#ebeb.e.eee.bbee...eee...ebb




