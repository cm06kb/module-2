
#
#def how_much_i_love_you(nb_petals):
#    x = ["I love you", "a little", "a lot", "passionately", "madly", "not at all"] 
#    n = (nb_petals-1)%(len(x))
#    print(n)
#    return x[n]
#
#print(how_much_i_love_you(461))
#
#def points(games):
#    
#    points = 0
#    for n in range(len(games)):
#        if (int(games[n][0]))>(int(games[n][2])):
#            points = points + 3
#        elif (int(games[n][0]))<(int(games[n][2])):
#            points = points 
#        else:
#            points = points + 1
#        
#    return points
#        
#print(points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']))


#def first_non_repeating_letter(string):
#    x = string.lower()
#    
#    if (string == ""):
#        return ""
#    else:
#        for n in x:
#            if (x.count(n)==1):
#                return string[x.index(n)]
        
        
#print(first_non_repeating_letter(''))

#def word_mesh(arr):
#    answer = []
#    for n in range(len(arr)-1):
#        word1 = arr[n]
#        word1_frg = []
#        for i in range(len(word1)):
#            word1_frg.append(word1[-(i+1):])
#            
#        word2 = arr[n+1]
#        word2_frg = []
#        for i in range(len(word2)):
#            word2_frg.append(word2[0:(i+1)])
#        
#        word1_frg = set(word1_frg)
#        word2_frg = set(word2_frg)    
#        sec = word1_frg.intersection(word2_frg)
#        if not sec:
#            break
#        else:
#            sec = list(sec)
#            sec = max(sec, key=len)
#            answer.append(sec)
#    
#    if len(answer) == len(arr)-1:
#        x = "".join(answer)
#        return x
#    else:
#        return "failed to mesh"
#       
#
#
#print(word_mesh(["beacone","condominium","umbilical","california"]))

#
#import math
#
#
#def easyline(n):
#    answer =[]
#    for k in range(n+1):
#        coeff = math.factorial(n)//(math.factorial(k)*math.factorial(n-k))
#        answer.append(coeff**2)
#    return sum(answer)
#
#print(easyline(38))
#
#


#def seven(m):
#    """
#        takes an int and checks whether it is divisible by 7.
#    """
#    steps = 0
#    new_num = 0
#    while len(str(m))>=2:
#        m_as_str = str(m)
#        last_num = int(m_as_str[-1])
#        print(last_num)
#        new_sec = m_as_str[0:-1]
#        new_sec = int(new_sec)
#        print(new_sec)
#        new_num = new_sec - (2* last_num)
#        m = new_num
#        if m % 7 == 0 and len(str(m))<=2:
#            steps = steps + 1
#            break
#        elif m%7 != 0  and len(str(m))==2:
#            steps = steps +1
#            break;
#        else:
#            steps = steps + 1
#
#    return new_num, steps
#            
#
#print(seven(1603))

#def order_weight(strng):
#    sep_strng = strng.split(" ")
#    list_nums = []
#    for n in sep_strng:
#        list_nums.append(int(n))
#    
#    
#
#print(order_weight("103 123 4444 99 2000"))

def correct(string):
    for n in string:
        if (n == "0"):
            string = string.replace("0", "O")
        elif (n == "5"):
            string = string.replace("5", "S")
        elif (n == "1"):
            string = string.replace("1", "I")
    return string


print(correct("L0ND0N"))      
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        











