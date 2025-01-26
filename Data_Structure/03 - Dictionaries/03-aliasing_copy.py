#Aliasing is the terme of pointing the same reference in data

inventory = {'mushroom': 14, 'apple': 4, 'mango': 6, 'orange':8}
print(inventory)
inventory_copy = inventory #aliasing - same data in memory
inventory_copy.update({'pinaple' : 12})
print(inventory)

supply = inventory.copy()
supply.update({'watermelon' : 10})
print(inventory)
print(supply)