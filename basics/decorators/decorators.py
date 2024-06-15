##################################################################################################
# author: ssmeherk
# date: 15.06.2024
# version: v1
# task/purpose: to read and display mobile numbers in uniform format
# source: https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem
##################################################################################################

def wrapper(func):                                                          # decorator func def

    def inner(mobile_list):                                                 # inner func
        updated_mobile_list = []                                            # initialize list
        for mb in mobile_list:
            # check for mobile num with 0 without space
            if len(mb) == 11:
                mb = mb[1:]
                mb = "+91 " + mb[:5] + " " + mb[5:]
                updated_mobile_list.append(mb)
            # check for mobile num with 91 without space
            elif len(mb) == 12:
                mb = mb[2:]
                mb = "+91 " + mb[:5] + " " + mb[5:]
                updated_mobile_list.append(mb)
            # check for mobile num with +91 without space
            elif len(mb) == 13:
                mb = mb[3:]
                mb = "+91 " + mb[:5] + " " + mb[5:]
                updated_mobile_list.append(mb)
            else:
                # if no additional digits are present
                mb = "+91 " + mb[:5] + " " + mb[5:]
                updated_mobile_list.append(mb)
                
        return func(updated_mobile_list)

    return inner


@wrapper                                                                    # decorator
def sort_mobile(random_list):                                               # sorted mobile func def
    print("Sorted Mobile Numbers:")
    print(*sorted(random_list), sep='\n')


@wrapper                                                                    # decorator
def unsorted_mobile(random_list):                                           # unsorted mobile func def
    print("Mobile Numbers:")
    print(*random_list, sep='\n')


if __name__ != '__main__':
    pass
else:
    read_list = []                                                          # initialize list
    with open("input-data", mode='r') as f:
        for item in f.readlines():
            read_list.append(item.strip())                                  # append data to list

    sort_mobile(read_list)                                                  # sorted mobile func call

    unsorted_mobile(read_list)                                              # unsorted mobile func call



