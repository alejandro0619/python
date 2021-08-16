# Lists are like Javascript's arrays:

friends = ["kevin", "karen", "Jim"]
# get the index:
friends[0] # will print out kevin 
friends[-1] # will print out Jim
friends[1:] # will print from karen on

friends[0:1] # will print from kevin to karen
friends[2] = "Juan" # modify elements


# Lists functions:
numbers1 = [1, 2, 3, 4, 5]
numbers2 = [6, 7, 8, 9]
#extends:
from_one_to_nine = numbers1.extend(numbers2) 
# adding elements:
numbers1.append(6)
#insert
numbers1.insert(0, 8) # first element will be 8
#remove:
numbers1.remove(1) # clean off the second index
#pop
numbers1.pop() # removes the last element on the list.
# find a elements index:
numbers1.index(4) # 5
#count how many times a elements shows up:
numbers1.count(4)
# sort ascending:
numbers1.sort()
# sort descending order:
numbers1.reverse()
# copy:
numbers3 = numbers1.copy()
