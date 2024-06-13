###########################################################################################
# author: ssmeherk
# date: 13.06.2024
# version: v1
# task/purpose: to demonstrate mathematical operations using numpy arrays
# source: https://www.hackerrank.com/challenges/np-array-mathematics/problem
############################################################################################
import numpy                                                            # import library
from contextlib import redirect_stdout

read_list = []                                                          # initialize list
with open("input-data", mode='r') as f:
    for item in f.readlines():
        read_list.append(item.strip())                                  # strip new line and append to list

rc = tuple(map(int, read_list.pop(0).split()))                          # rows and cols as tuple

# initialize two lists for two input arrays
list_one = []
list_two = []

# append values to list
for item in range(0, rc[0]):
    list_one.append(list(map(int, read_list.pop(0).split())))

# append values to list
for item in range(0, rc[0]):
    list_two.append((list(map(int, read_list.pop(0).split()))))

arr_one = numpy.array(list_one)                                         # list to array arr_ome
arr_two = numpy.array(list_two)                                         # list to array arr_two

with open("output-data", mode='w') as f:
    with redirect_stdout(f):                                            # redirect stdout to a file
        # mathematical operations using numpy arrays
        print(numpy.add(arr_one, arr_two))
        print(numpy.subtract(arr_one, arr_two))
        print(numpy.multiply(arr_one, arr_two))
        print(numpy.floor_divide(arr_one, arr_two))                     # floor division
        print(numpy.mod(arr_one, arr_two))
        print(numpy.power(arr_one, arr_two))