#!/usr/bin/python3
##############################################################################################
# author: ssmeherk
# date: 19.06.2024
# version: v1
# task/purpose: to determine subscribers of english or french but not both
# source: https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem
###############################################################################################

input_list = []

with open("input-data", mode='r') as f:
    for item in list(f.readlines()):
        input_list.append(item.strip())

n = int(input_list[0])                              # read number of eng students
engset = set(map(int, input_list[1].split()))       # set of roll num of eng students

b = int(input_list[2])                              # read num of french students
frenset = set(map(int, input_list[3].split()))      # set of roll num of fren students

# total no.of students in eng or french but not both
count = len(engset.symmetric_difference(frenset))   # using symmetric_difference() method

# print the final count
print(count)
