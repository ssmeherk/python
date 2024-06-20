#!/usr/bin/python3
############################################################################
# author: ssmeherk
# date: 20.06.2024
# version: v1
# task/purpose: get the captain's room number
# source: https://www.hackerrank.com/challenges/py-the-captains-room/problem
#############################################################################

read_list = []
with open("input-data", mode='r') as f:
    for item in f.readlines():
        read_list.append(item.strip())

K = int(read_list[0])                                       # read size of group
rooms = list(map(int, read_list[1].split()))                # read input room numbers
rooms_set = set(rooms)

# checks for room num in the rooms
for item in rooms_set:
    if item in rooms:
        rooms.remove(item)                                  # removes room num from list

rooms_updated_set = set(rooms)

# difference between original rooms_set and updated_rooms_set
for capt_room in rooms_set.difference(rooms_updated_set):
    print("Captain's Room Number:",capt_room)
