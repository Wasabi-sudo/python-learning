inventory = {'mushroom': 14, 'apple': 4, 'mango': 6, 'orange':8}

#Add or Update data
inventory.update({'banana': 10})
inventory.update({'apple': 100})

print(inventory)

inventory.update({'pear': 23, 'lemon': 15})
print(inventory)

#Remove a data
inventory.pop('orange')
inventory.pop('orange', 'There is no more this data')

del inventory['mango']

print(inventory)

#del last elem
inventory.popitem()
print(inventory)

#delete all
inventory.clear()
print(inventory)