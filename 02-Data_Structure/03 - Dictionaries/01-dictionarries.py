# Dictonaries are a K,V liste

supply = {'apple': 4, 'mango': 6, 'orange':8}
print(type(supply))
print(supply)

basket = dict(lemon = 2.2)
print(basket)

#Add element
basket['cherry'] = 65
print(basket)

inventory = {'orange': {'price' : 1.5, 'stock': 45},
             'lemon': {'price' : 0.4, 'stock': 35}}
print(inventory)
print(inventory['orange']['price'])

#Converting lists into dictionaries
products = ['orange', 'lemon']
prices = [1.2, 0.9]

print(type(zip(products, prices)))
print(type(dict(zip(products, prices))))

cart = dict(zip(products, prices))
print(cart)

print('-----------------------------------------------------')
inventory = {'mushroom': 14, 'apple': 4, 'mango': 6, 'orange':8}
print(inventory)

#Sum
sumInventory = sum(inventory.values())
print(sumInventory)

#Keys
keys = inventory.keys()
print(keys)

#Items
items = inventory.items()
print(items)

sorted(inventory.keys(), reverse=True)
print(inventory)

#Member
'orange' in inventory

#Retrieve values without error
inventory.get('lemon')
inventory.get('lemon', 'There is no lemon in the liste')





