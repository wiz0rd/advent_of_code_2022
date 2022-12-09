from collections import OrderedDict
import pprint

leng = 0
height = 0
stopper = 0
with open('input.txt', 'r') as r:
    for line in r:
        line = line.strip()
        height += 1
        if stopper == 0:
            leng = len(line)
            stopper += 1

circumference = (leng * 2) + (height * 2) - 4
#print(circumference)


##Make Tree Grid ##
trees = OrderedDict()
for number in range(height):
            trees[number] = []
with open('input.txt', 'r') as r:
    counter = 0
    for line in r:
        line = line.strip()
        for num in list(line):
            trees[counter].append(num)
        counter += 1

## Make Tree Score Board
visible_trees = OrderedDict()
for number in range(height):
    visible_trees[number] = []

visible_tree_counter = 0
for number in range(height):
    for numby in range(leng):
        visible_trees[number].append('O')


for number in range(len(visible_trees)):
    visible_trees[0].pop()
    visible_trees[height - 1].pop()
for number in range(len(visible_trees)):
    visible_trees[0].append('X')
    visible_trees[height - 1].append('X')
for number in range(height):
    visible_trees[number][0] = 'X'
    visible_trees[number][-1] = 'X'

for k,v in visible_trees.items():
    key_tracker = k
    #print(key_tracker)
    value_tracker = 0
    for tree in v:
        if tree == 'O':
            ## looking good but lots of work here ##
            ##print(trees[k][value_tracker])
            value_tracker += 1
        elif tree == 'X':
            value_tracker += 1

row_tracker = 1

#for k in trees.keys():
#    column_tracker = 1
#    if k != 0 and k != leng:
#      if trees[k][column_tracker] > trees[k - 1][column_tracker]:
#            visible_trees[k][column_tracker] = 'X'
#    upcolumn_tracker += 1

## Check the vertical axis from the top down Column by Column ##
## YAY vertical done from top down!
columns_to_check_from_top = []
rows_to_check_from_top = []

for number in range(leng):
    columns_to_check_from_top.append(number)

del columns_to_check_from_top[0]
del columns_to_check_from_top[-1]

for number in range(height):
    rows_to_check_from_top.append(number)

del rows_to_check_from_top[0]

for number in rows_to_check_from_top:
    for num in columns_to_check_from_top:
        if trees[number][num] > trees[number -1][num]:
            visible_trees[number][num] = 'X'
        else: break

## Work the bottom up!##
columns_to_check_from_bottom = []
rows_to_check_from_bottom = []

for number in range(leng):
    columns_to_check_from_bottom.append(number)

columns_to_check_from_bottom.reverse()
del columns_to_check_from_bottom[0]
del columns_to_check_from_bottom[-1]

print(columns_to_check_from_bottom)
for number in range(height):
    rows_to_check_from_bottom.append(number)
del rows_to_check_from_bottom[-1]
print(rows_to_check_from_bottom)

for number in rows_to_check_from_bottom:
    for num in columns_to_check_from_bottom:
        if trees[number][num] > trees[number +1][num]:
            visible_trees[number][num] = 'X'
        else: break




pp = pprint.PrettyPrinter(indent=4)
pp.pprint(trees)
print('\n')
pp.pprint(visible_trees) 

 