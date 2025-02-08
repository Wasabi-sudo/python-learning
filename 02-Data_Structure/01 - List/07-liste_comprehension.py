"""
[expression for élément in iterable if condition]
"""

elements = range(10)
carrés = [x**2 for x in elements]
print("Carrés:", carrés) 


pairs = [x for x in range(10) if x % 2 == 0]
print("Nombres pairs:", pairs)


mots = ["python", "est", "génial"]
majuscules = [mot.upper() for mot in mots]
print("Mots en majuscules:", majuscules) 



# Création d'une liste de tuples
coordonnées = [(x, y) for x in range(3) for y in range(2)]
print("Coordonnées:", coordonnées)



# Utilisation de `if-else` dans une list comprehension
parité = ["pair" if x % 2 == 0 else "impair" for x in range(5)]
print("Parité:", parité)




"""
Différence entre List Comprehension et Générateur
--------------------------------------------------
- Une **list comprehension** crée une **liste complète** en mémoire.
- Une **generator expression** génère les valeurs **à la demande**, sans stocker tout en mémoire.

Exemple de générateur :
"""

gen = (x**2 for x in range(10))
print("Générateur:", gen)  # Output: <generator object <genexpr> at 0x...>
print(next(gen))  # Output: 0
print(next(gen))  # Output: 1

# Transformer un générateur en liste
gen_list = list(x**2 for x in range(5))
print("Liste depuis générateur:", gen_list)  # Output: [0, 1, 4, 9, 16]
