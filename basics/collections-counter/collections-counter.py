#!/usr/bin/python3
###############################################################################
# author: ssmeherk 
# date: 21.06.2024
# version: v1
# task/purpose: to print the amount of money earned
# source: https://www.hackerrank.com/challenges/collections-counter/problem
################################################################################
from collections import Counter

read_list = []                                                      # initialize list
# read input data as list from file
with open("input-data", mode='r') as f:
    for item in f.readlines():
        read_list.append(item.strip())

shoes_count = int(read_list.pop(0))                                 # read shoes_count
shoes = list(map(int, read_list.pop(0).split()))                    # read shoe sizes

customer_count = int(read_list.pop(0))                              # read customer count
size_and_price = []                                                 # initialize list

amount = 0

# find the right size from shoes and add the amount
for i in range(0, customer_count):
    size_and_price = list(map(int, read_list.pop(0).split()))
    if size_and_price[0] in Counter(shoes).keys():
        amount += size_and_price[1]
        shoes.remove(size_and_price[0])
        
print("Amount of money earned:", amount)
