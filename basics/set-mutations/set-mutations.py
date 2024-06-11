#!/usr/bin/python3
###################################################################################
# author: ssmeherk
# date: 11.06.2024
# version: v1
# task/purpose: to demonstrate set mutation operations
# source: https://www.hackerrank.com/challenges/py-set-mutations/problem
####################################################################################
input_list = []                                                         # initialize an empty list

with open("input-data", mode='r') as f:                                 # read input data
    for item in f.readlines():
        input_list.append(item.strip())                                 # strip new line char and append to list

# print(input_list)
# print(len(input_list))

a_count = int(input_list.pop(0))                                        # pop off & store first item of the list
a_set = set(map(int, input_list.pop(0).split()))                        # create a set from the new first item
print("Initial Input, Set A: ", a_set)

n = int(input_list.pop(0))                                              # pop off new first item & store in n
n_count = n * 2

# print(input_list)
# print(len(input_list))

for i in range(0, len(input_list)):
    # print(input_list[0].split()[0])
    if input_list[i].split()[0] == 'intersection_update':               # check for the right command
        len_int_update_set = int(input_list[i].split()[1])
        # print(len_int_update_set)
        int_update_set = set(map(int, input_list[i+1].split()))         # create set on which the command is executed
        # print(int_update_set)
        a_set.intersection_update(int_update_set)                       # execute the command
        print("After intersection_update operation, set A: ", sorted(a_set))
    elif input_list[i].split()[0] == 'update':                          # check for the right command
        len_update_set = int(input_list[i].split()[1])
        update_set = set(map(int, input_list[i+1].split()))             # create set on which the command is executed
        a_set.update(update_set)                                        # execute the command
        print("After update operation, set A: ", sorted(a_set))
    elif input_list[i].split()[0] == 'symmetric_difference_update':     # check for the right command
        len_sym_diff_upd_set = int(input_list[i].split()[1])
        sym_diff_upd_set = set(map(int, input_list[i+1].split()))       # create set on which the command is executed
        a_set.symmetric_difference_update(sym_diff_upd_set)             # execute the command
        print("After symmetric_difference_update operation, set A: ", sorted(a_set))
    elif input_list[i].split()[0] == 'difference_update':               # check for the right command
        len_diff_upd_set = int(input_list[i].split()[1])
        diff_upd_set = set(map(int, input_list[i+1].split()))           # create set on which the command is executed
        a_set.difference_update(diff_upd_set)                           # execute the command
        print("After difference_update operation, set A: ", sorted(a_set))

print("Sum of elements in set A: ", sum(a_set))                         # sum of final set of elements


