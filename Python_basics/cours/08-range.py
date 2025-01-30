#range function returns a sequence of numbers (list)


#same
list = range(7) # => (0,1,2,3,4,5,6,7)
print(list)

list = range(0, 7) # => (0,1,2,3,4,5,6,7)
print(list)

list = range(0, 7, 1) # => (0,1,2,3,4,5,6,7)
print(list)


#diff
list = range(2, 14, 2) # => (2,4,6,8,10,12)
print(list)

for i in range(7):
    print(i)