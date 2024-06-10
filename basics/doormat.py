#############################################################################
# author: ssmeherk
# date: 10.06.2024
# version: v1
# purpose/task: to draw a welcome doormat
# source: https://www.hackerrank.com/challenges/designer-door-mat/problem
#############################################################################

import shutil

# get_terminal_size() gets the size of terminal window with columns & lines
# columns stores the number of columns of the terminal
columns = shutil.get_terminal_size().columns

print("Please enter an odd natural number:")
N = int(input())                                # read and store the input as int
if N % 2 == 0 or N <= 0:                        # checks whether input is not an odd natural number
    print("Provided input is not an odd natural number.")
    print("Please try again. Thank you!!")
    exit()

M = 3*N                                         # number of columns (M) is 3 times number of rows (N)

dot = ".|."
hyphen = "-"

welcome = "WELCOME"
len_welcome = len(welcome)                      # length of string

center_line = (M - len(welcome))/2

# top half of the doormat design
for i in range(1, N, 2):
    output = (hyphen * int((M - (i*len(dot)))/2) + (dot * i) + (hyphen * int((M - (i*len(dot)))/2)))
    print(output.center(columns))               # prints the output at the center of the terminal window

# center of the doormat design that prints welcome message
output = (hyphen * int(center_line)) + welcome + (hyphen * int(center_line))
print(output.center(columns))                   # prints the output at the center of the terminal window

# bottom half of the doormat design
for i in range(N - 2, 0, -2):
    output = (hyphen * int((M - (i*len(dot)))/2) + (dot * i) + (hyphen * int((M - (i*len(dot)))/2)))
    print(output.center(columns))               # prints the output at the center of the terminal window
