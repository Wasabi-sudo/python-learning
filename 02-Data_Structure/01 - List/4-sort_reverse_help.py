products = ['mango', 'banana', 'pickels', 'orange', 'castore','apple']
print(products)

products.sort()
print(products)


products.sort(reverse=True)
print(products)

products.reverse()
print(products)


robot = ['XWX554', 'XWX544', 'XWX987']


products.extend(robot)
print(products)

newlist = products + robot
print(newlist)
#help(products)

counting= newlist.count('XWX554')
print(counting)