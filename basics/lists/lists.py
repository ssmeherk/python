#!/usr/bin/python3
#########################################################################
# author: ssmeherk
# date: 06.06.2024
# version: v1
# purpose/task: to take input from a file and run various list commands
# source: hackerrank
#########################################################################

# function definition
def run_list_commands():
    input_list = []
    output_list = []

    # read the input file and append to list without newline
    with open("input-lists", mode='r') as f:
        for item in list(f.readlines()):
            input_list.append(item.strip())

        # pops off index 0 item from the list
        num = int(input_list.pop(0))

        for i in range(0, num):
            command, *items = input_list[i].split()     # unpacking operator to split command & its parameters
            items = list(map(int, items))               # convert list items to int type

            # checks the right command and execute it
            if command == "insert":
                output_list.insert(items[0], items[1])
            elif command == "print":
                print(output_list)
            elif command == "remove":
                output_list.remove(items[0])
            elif command == "append":
                output_list.append(items[0])
            elif command == "sort":
                output_list.sort()
            elif command == "pop":
                output_list.pop()
            elif command == "reverse":
                output_list.reverse()


if __name__ == "__main__":
    # function call
    run_list_commands()
