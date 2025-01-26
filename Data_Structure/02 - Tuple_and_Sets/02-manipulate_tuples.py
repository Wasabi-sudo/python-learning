mango = ('fruits', 1.4, [10,15])
lemon = ('fruits', 0.9, [5,8])

# dir(mango) - liste info tuple method

#concatenate tuple
fruits = mango + lemon

print(fruits)


#unpacking tuple

toto = (apple, tomato, pinaple) = ('1', '2', '3')
print(toto)
print(apple)


#Add _ to complite the missing tuple
toto = (apple, tomato, pinaple, _) = ('1', '2', '3', '4')
print(toto)

#Add * to complite the missing tuple
toto = (apple, tomato, *pinaple) = ('1', '2', '3', '4', '5', '6', '7', '8')
print(toto)
print(pinaple) #Had all the rest of the data in a liste

