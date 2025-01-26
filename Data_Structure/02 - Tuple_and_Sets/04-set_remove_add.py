categories = {'fruits', 'coffee', 'vegetables', 'candy', 'coffee', 'candy'}
print(type(categories))
print(categories)

#Remove elements
categories.discard('candy') #preférable a remove() car ne lève pas d'erreur si il n'existe pas
print(categories)

isCadyInSet = 'candy' in categories
print(isCadyInSet)

categories.remove('coffee')
print(categories)

#Adding element
categories.add('seafood')
print(categories)

categories.add('fruits') #already exist so nothing happend
print(categories)

#Insert multiple elements use update
new_categorie = {'elec', "clothing"}
categories.update(new_categorie)
print(categories)

#Pop - delete a random value of a set
categories.pop()
print(categories)