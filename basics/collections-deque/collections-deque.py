#!/usr/bin/python3
##############################################################################
# author: ssmeherk
# date: 22.06.2024
# version: v1
# task/purpose: demonstrate various double ended queue methods
# source: https://www.hackerrank.com/challenges/py-collections-deque/problem
##############################################################################
from collections import deque

input_list = []                                         # initialize list

# read file and store data in input_list line by line
with open("input-data", mode='r') as f:
    for item in f.readlines():
        input_list.append(item.strip())

N = int(input_list.pop(0))                              # read number of command lines
d = deque()                                             # initialize deque

# checks for command from input_list and execute the command
for i in range(0, N):
    comm, *item = input_list.pop(0).split()
    if comm == 'append':
        d.append(item)
    elif comm == 'appendleft':
        d.appendleft(item)
    elif comm == 'pop':
        d.pop()
    elif comm == 'popleft':
        d.popleft()
    else:
        pass

# print deque output as space separated elements
s = ""                                                  # initialize a string
for elem in d:
    s += elem[0] + " "                                  # concatenate deque elements to string

print("Space separated elements of deque:", d, "is", s)

