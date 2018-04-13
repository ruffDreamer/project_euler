'''
Created on May 15, 2015

@author: morpheus
'''
import math
def factorcount(a):
    y=0
    for x in range(int(math.floor(math.sqrt(a))),0,-1):
        if a % x == 0:
            y=y+1  
    return 2*y
 
def trinum(a):
    return int(a*(a+1)/2)
x=2
while factorcount(trinum(x))<=500:
     x=x+1;
     print(trinum(x))
     
