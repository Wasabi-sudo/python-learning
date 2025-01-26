"""
Set are not ordered
set don't record element position
Set don't allow duplicates

They are useful to get a unique element in a dataset

they are mutable
They can be transforme into a immutable sets with frozenset() command

!! Set a mutable BUT their elements must be immutable !! (cannot have list in a set)
"""

myset = {}
myset2 = set()
#--------------------------#

product_list = ['fruits', 'coffee', 'vegetables', 'candy', 'coffee', 'candy']
print(product_list)

product_set = set(product_list)
print(product_set)
print(type(product_set))

test = {}
print(type(test))

test2 = {'myelement', 'otherelement'}
print(type(test2))

test3 = {'1', '2', '1'}
print(test3)
print(type(test3))
