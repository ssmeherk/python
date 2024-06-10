########################################################################################
# author: ssmeherk
# date: 10.06.2024
# version: v1
# task/purpose: to generate a list of cube of fibonacci numbers
# source: https://www.hackerrank.com/challenges/map-and-lambda-expression/problem
#########################################################################################


cube = lambda x: x**3       # lamba function calculating cube of each number

def fibonacci(n):

    fib = []                # initialize an empty list

    if n == 0:              # return empty list if n is zero
        pass
    elif n == 1:            # adds zero to the list and returns
        fib.append(0)
    else:
        fib = [0, 1]        
        while len(fib) < n:                 # adds previous two numbers of the list
            fib.append(fib[-1] + fib[-2])   # and appends to the list
    
    return fib                              # returns list of fibonacci numbers
        

if __name__ == '__main__':
    print("Please enter a number:")
    n = int(input())                        # Read and stores input as integer
    print(list(map(cube, fibonacci(n))))    # prints list of cube of fibonacci numbers
