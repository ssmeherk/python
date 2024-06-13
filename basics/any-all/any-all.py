#################################################################################
# author: ssmeherk
# date: 13.06.2024
# version: v1
# task/purpose: given a space separated list of integers.
#               if all the integers are positive,
#               then you need to check if any integer is a palindromic integer.
#               demonstrate using any and all builtin functions
# source: https://www.hackerrank.com/challenges/any-or-all/problem
##################################################################################

read_list = []
with open("input-data", mode='r') as f:
    for item in f.readlines():
        read_list.append(item.strip())

n = int(read_list.pop(0))                            # read num of integers
n_list = list(read_list.pop(0).split())              # read integers as string

# check if all elements of list are positive numbers
first_check_list = []                       # initialize list
# append +ve integer condition to each element of the list
for i in range(0, len(n_list)):
    first_check_list.append(int(n_list[i])>0)

# check for all elements of list and return True or False
first_check = all(first_check_list)

if first_check is True:
    # check if all elements of list are palindrome integers
    second_check_list = []                  # initialize list
    for i in range(0, len(n_list)):
        # append palindrome condition to each element of the list
        second_check_list.append(n_list[i] == n_list[i][::-1])
        
    # checks if any of the elements of list is True
    # and returns True
    second_check = any(second_check_list)
    if second_check is True:
        print("Palindromic integer is present in the given integers")
    else:
        print("No presence of palindromic integer")
else:
    print("All the given integers are not positive")







