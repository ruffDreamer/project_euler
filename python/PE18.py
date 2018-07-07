#!/usr/bin/python

#max function
def max(a,b):
    if a < b:
        return b
    else:
        return a

#open text file and make empty list
f = open("/Users/jordand/Documents/github/project_euler/python/PE18.txt", 'r')
triangle =[]

#add each line of text file to list as a new entry
for index,line in enumerate(f):
    triangle.append(line.strip().split(' '))

#convert each string element to an int
for index1,list in enumerate(triangle):
    for index2,item in enumerate(list):
        triangle[index1][index2] = int(triangle[index1][index2])
#print triangle

#calculate max last row
def best_path_last_row(list):
    max_row = []
    for x in range(len(list[len(list)-2])):
        max_row.append(max(list[len(list)-2][x] + list[len(list)-1][x], list[len(list)-2][x] + list[len(list)-1][x+1]))
    return max_row

def best_path_sum(list):
    while len(list) > 1:
        list[len(list)-2] = best_path_last_row(list)
        list.pop()
    return list

print(best_path_sum(triangle))

