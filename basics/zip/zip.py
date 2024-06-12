#!/usr/bin/python3
##############################################################################
# author: ssmeherk
# date: 12.06.2024
# version: v1
# task/purpose: to calculate average of marks for each students using zip
# source: https://www.hackerrank.com/challenges/zipped/problem
##############################################################################

from contextlib import redirect_stdout                      # context manager to redirect output to a file

read_list = []

with open("input-data", mode='r') as f:                     # read input-data, strip new line and
    for item in f.readlines():                              # store in a list
        read_list.append(item.strip())

N, X = list(map(int, read_list.pop(0).split()))                 # read N and X

input_list = []                                                 # initialize list

for i in range(0, X):                                           # create subject-wise list
    input_list.append(list(map(float, read_list.pop(0).split())))

# open output-data and redirect output to the file
with open("output-data", mode='w') as f:
    with redirect_stdout(f):
        for item in zip(*input_list):                           # zip creates student-wise tuple
            print("{0:0.1f}".format(sum(item)/X))               # average score of each student

