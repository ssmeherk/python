#!/usr/bin/python3
###############################################################
# author: ssmeherk
# date: 24.05.2024
# version: v1
# purpose/task: usage of if-else condition
################################################################

# function definition
def check_num():
    print("Enter any positive integer between 1 to 100: ")
    n = int(input())

    # check if number is even or odd and
    # print the statement based on its range
    if n % 2 == 0:
        if 2 <= n <= 5:
            print("Input number between 2 to 5")
        elif 6 <= n <= 20:
            print("Input number between 6 to 20")
        else:
            print("Input number greater than 20")
    else:
        print("Input number is odd")


if __name__ != '__main__':
    pass
else:
    # function call
    check_num()
