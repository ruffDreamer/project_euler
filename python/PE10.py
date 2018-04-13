#!/usr/bin/python3
import math
def isprime(a):
    if a == 2:
        return True
    elif a == 3:
        return True
    else:
        for x in range(int(math.ceil(math.sqrt(a))),1,-1):
            if a % x == 0:
                test = False
                break
            else:
                test = True
    return test
           
x=0
for prime in range(2,2000001,1):
    if isprime(prime):
        x=x+prime
        print (x)
          
