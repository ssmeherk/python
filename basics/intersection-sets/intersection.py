#!/usr/bin/python3
####################################################################################
# author: ssmeherk
# date: 11.06.2024
# version: v1
# task/purpose: to determine subscribers of both english and french using sets
# source: https://www.hackerrank.com/challenges/py-set-intersection-operation/problem
####################################################################################

input_list = []

with open("input-data", mode='r') as f:
    for item in list(f.readlines()):
        input_list.append(item.strip())

n = int(input_list[0])                            # read number of eng students
engset = set(map(int, input_list[1].split()))     # set of roll num of eng students

b = int(input_list[2])                            # read num of french students
frenset = set(map(int, input_list[3].split()))    # set of roll num of fren students


# roll  num of students subscribed to eng but not french
ef_set = engset.difference(frenset)
# roll num of students subscribed to french but not english
fe_set = frenset.difference(engset)


# roll num of students who are subscribed to only one
ef_fe_union = ef_set.union(fe_set)
# roll number of all students
engfen_union = engset.union(frenset)


# roll num of students subscribed to both english and french
engfen_both = engfen_union.difference(ef_fe_union)
print("List of students subscribed to both englisth and french: ", engfen_both)

# prints the count
print("Number of students subscribed to both english and french: ", len(engfen_both))

