x = [4,7,5,2,8,1,7]

print(x)

print(x[1])

print(x[-1])

#interval
print(x[1:4])

intervale = x[1:4]
print('intervale type :', type(intervale))

#Print all the liste
print(x[:])

#All element in the begin of the list until 3 index
print(x[:3])

#All element in the end of the list until last 3 index
print(x[3:])

#Find the first index of a specific element
print('index:', x.index(7))


print('longueur:', len(x))

print('max:', max(x))

print('sum:', sum(x))

print ('---------------------------------')


y = ['toto', 'tata', 'tutu', 'aaaa']

print(y)

print('longueur:', len(y))
print('max:', max(y))
#print('sum:', sum(y)) Exception! Not supported on str

#Findthe index of a specific element
print('index:', y.index('tutu'))

print('tutu' in y)
print('titi' in y)
print('titi' not in y)

print ('---------------------------------')

z = ['toto', 'tata', 'tutu', 'aaaa', 1, 213, 564 , 89,  221, 6]

print(z)

#print('max:', max(z)) / Not supported between int and str

print ('---------------------------------')