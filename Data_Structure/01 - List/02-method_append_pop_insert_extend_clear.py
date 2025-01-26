"""
    Methods de manipulation de liste
-> append, remove, insert, extend, pop, clear <-

"""
# A "method" is a function built in into a specific data structure; {x,y}

#Creating list
products = ['apple', 'banana', 'orange', 'mango']

#Calling the len "function"
len(products)

#Calling the append "method1"
#Ajoute un element a la fin de la liste
products.append('lemon')
print(products)

#Remove LAST elements in the liste
products.pop()
print(products)

products.remove('apple')
print(products)

#Ajoute un element a un index specifique
products.insert(1, 'lemon')
print(products)

#Concate liste
electronics = ['TV', 'laptop']
products.extend(electronics)
print(products)

#Remove all element
electronics.clear()
print(electronics)

#AJOUTE SANS COPIE 
products.extend(electronics)
print(products)

for i in range(1, 101):
    if (i % 3 == 0 and i % 5 == 0):
        print('FizzBuzz')
    elif(i % 5 == 0):
        print('Buzz')
    elif(i % 3 == 0):
        print('Fizz')
    else:
        print(i)
    
