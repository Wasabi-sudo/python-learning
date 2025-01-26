#tuple are more performant than list
# but there are immutable (peux pas etre changer)

mylist = [1,2,3,5,6]
mytuple = (1,21,'toto',5,6, [1,42,5])

print(mytuple)

#mytuple[1] = 42 -> Will product a error / because tuple is immutable


"""To do so we need to convert a tuple to a list"""

#Convert tuple to list
mylist = list(mytuple)
print(mylist)


#Convert list to tuple
mytuple = tuple(mylist)
print(mytuple)

#Altering mutable object in immutable tuple
mytuple[-1][2] = 100
print(mytuple)