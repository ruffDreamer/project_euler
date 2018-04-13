#!/usr/bin/python3
pythBool = False
a=0
while a<1000 and not pythBool:
    b=a
    a=a+1
    while b<1000:
        b=b+1
        c=1000-a-b
        if a**2+b**2==c**2:
            pythBool = True
            prod=a*b*c
            break
print (prod)        
