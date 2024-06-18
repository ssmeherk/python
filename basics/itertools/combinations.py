######################################################################################
# author: ssmeherk
# date: 18.06.2024
# version: v1
# task/purpose: to print all possible combinations of the string S, up to size k, 
#               in lexicographic sorted order.
# source: https://www.hackerrank.com/challenges/itertools-combinations/problem
######################################################################################
from itertools import combinations

print("Please enter a string in CAPITAL letters:")
S = input().upper()
len_S = len(S)

print("Please enter the size (up to which the possible combinations should be printed):")
k = int(input())

if k < 0 or k > len_S:
    print("Error: Size should be between 0 and length of the input string")
    print("Please enter correct input")
    exit(1)

output_list = []

print("Combinations of the input string", S, "up to size", k, ":")

for i in range(1, int(k)+1):
    output_list = list(combinations(sorted(S), i))
    for tup in output_list:
        print("".join((map("".join, tup))))
        

