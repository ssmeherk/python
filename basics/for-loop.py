#!/usr/bin/python3
##################################################################
# author: ssmeherk
# date: 25.05.2024
# version: v1
# purpose/task: to print square of each number using for loop
##################################################################
# function definition
def square_num():
    print("Enter any positive integer between 1 to 20: ")
    num = int(input())

    # check if the input number is in the given range and
    # proceed for squaring of each number using for loop
    if 1 <= num <= 20:
        for i in range(num):
            print(i * i)
    else:
        print("Entered number is not in between 1 to 20")


if __name__ == "__main__":
    # function call
    square_num()
