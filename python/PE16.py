#!/usr/bin/python3

def digit_count(value):
    sum = 0
    for x in str(value):
        sum += int(x)
    return sum

print(digit_count(2**1000))
