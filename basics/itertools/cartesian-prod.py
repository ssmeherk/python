################################################################################
# author: ssmeherk
# date: 14.06.2024
# version: v1
# task/purpose: given two lists A & B, compute their cartesian product (AXB)
# source: https://www.hackerrank.com/challenges/itertools-product/problem
################################################################################
from itertools import product

print("Please enter space separated integers for list A:")
A = list(map(int, input().split()))                                         # read space separated integer input
print("Please enter space separated integers for list B:")
B = list(map(int, input().split()))                                         # read space separated integer output

cart_prod = list(product(A, B))                                             # cartesian product

print("Cartesian Product,AXB:",' '.join(map(str, sorted(cart_prod))))       # space separated output

