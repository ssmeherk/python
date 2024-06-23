####################################################################################
# author: ssmeherk
# date: 23.06.2024
# version: v1
# task/purpose: to print the indexed positions of the occurences of the word
# source: https://www.hackerrank.com/challenges/defaultdict-tutorial/problem
#####################################################################################
from collections import defaultdict

read_list = []
with open("input-data", mode='r') as f:
    for item in f.readlines():
        read_list.append(item.strip())

for i in range(len(read_list)):
    line = read_list[0]
    if line[0] == '#':
        read_list.pop(0)

print("Input items as list:",read_list)

n, m = read_list.pop(0).split()

group_a = []
group_b = []

da = defaultdict(list)
db = defaultdict(list)


for i in range(1, int(n)+1):
    da[i].append(read_list.pop(0))

print("Grouped items as dictionary:", da)

for i in range(1, int(m)+1):
    db[i].append(read_list.pop(0))

print("Grouped items as dictionary:", db)

# for i in db:
#    item = db[i]
#    for j in da:
#        if da[j] == item:
#            print(j)

print("Space separated indexed positions:")
for i in db:
    item = db[i]
    value = [j for j in da if da[j] == item]
    if value == []:
        value.append(-1)
    print(" ".join(map(str, value)))

