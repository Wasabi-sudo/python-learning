class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
        print('Woof Woof!\n')

#Main
dog = Dog('Chips', 'Husky')
print(dog.name, " : ", dog.breed)
dog.bark()