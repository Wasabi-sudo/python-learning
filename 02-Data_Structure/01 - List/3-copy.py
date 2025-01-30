A = [1,2,3,5,9,4]
print('A', A)

# ! A et B partage le meme espace mémoire / si l'un change l'autre aussi
B=A
print('B', B)

B.append(42)
print('A:', A)
print(A is B)

#Pour copier correctement une liste et donc dupliqué la data il faut utilisé list()

B = list(A)
print(A is B)

B.append(32)
print('A', A)
print('B', B)

