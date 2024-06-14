##############################################################################
# author: ssmeherk
# date: 14.06.2024
# version: v1
# task/purpose: to print all possible permutations of size k,
#               of the string s, in lexicographic sorted order using itertools
# source: https://www.hackerrank.com/challenges/itertools-permutations/problem
###############################################################################
from itertools import permutations

print("Enter a string in CAPITAL LETTERS:")
s = input()                                                                 # input string
len_s = len(s)                                                              # length of input string

print("Enter a positive integer (length of permutations of elements):")
k = int(input())                                                            # length of permutation of elements
try:
    permutation_list = list(permutations(s, int(k)))                        # permutation list of tuples
except ValueError:
    print("Input integer cannot be less than zero")                         # catches k < 0 exception
    exit(1)

# combine elements of tuple as a single string without space
combined_list = list(map(''.join, sorted(permutation_list)))

print("Permutations of the string", s, ":")

for item in combined_list:                                                  # print output on separate lines
    print(item)
