#!/usr/bin/python3

def pathset(size):
    success = []
    list = ['0','1']
    for x in range(2*size-1):
        list += list
        for y in range(len(list)/2):
            list[y] += '0'
        for z in range(len(list)/2,len(list)):
            list[z] += '1'
    for item in list:
        if item.count('0') == item.count('1'):
            success.append(item)
    return success

print("What is the size of the grid?")
value = input()
print(len(pathset(value)))
