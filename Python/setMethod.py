
# creating am empty set
from os import remove


b = set()
print(type(b))

# adding values to an empty set
b.add(4)
b.add(5)
b.add((4,5,6)) # add tuples in set
print(b)

# Cannot add list or dictionary to sets

print(len(b)) # prints the length of set

b.remove(5) # remove 5 of set
print(b)

print(b.pop())
print(b) 