#!/usr/bin/python3

def word_sum(value):
    sum = 0
    con_fact = {"0" : "","00" : "","1" : "one","2" : "two","3" : "three","4" : "four","5" : "five","6" : "six","7" : "seven","8" : "eight","9" : "nine","10" : "ten","11" : "eleven","12" : "twelve","13" : "thirteen","14" : "fourteen","15" : "fifteen","16" : "sixteen","17" : "seventeen","18" : "eighteen","19" : "ninetine","20" : "twenty","30" : "thirty","40" : "forty","50" : "fifty","60" : "sixty","70" : "seventy","80" : "eighty","90" : "ninety","100" : "hundred","1000" : "thousand"}

    for x in range(1,value + 1 ):
        if x < 21:
            sum += len(con_fact[str(x)])
        elif x >= 21 and len(str(x)) == 2:
            sum += len(con_fact[str(x)[0] + '0']) + len(con_fact[str(x)[1]])
        elif len(str(x)) == 3:
            if int(str(x)[-2:]) < 10:
                if str(x)[-2:] == '00':
                    sum += len(con_fact[str(x)[0]]) + len(con_fact["100"])
                else:
                    sum += len(con_fact[str(x)[0]]) + len(con_fact["100"]) + 3 + len(con_fact[str(x)[-1:]])
            elif int(str(x)[-2:]) >= 11 and int(str(x)[-2:]) < 20:
                sum += len(con_fact[str(x)[0]]) + len(con_fact["100"]) + 3 + len(con_fact[str(x)[-2:]])
            else:
                sum += len(con_fact[str(x)[0]]) + len(con_fact["100"]) + 3 + len(con_fact[str(x)[1] + '0']) + len(con_fact[str(x)[2]])
        else:
            sum += len(con_fact["1"]) + len(con_fact["1000"])
    return sum

print(word_sum(1000))

