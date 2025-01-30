acronyms = ['LOL', 'IDK', 'TOTO']
print(acronyms)

acronyms = []
acronyms.append('TITI')
acronyms.append('TUTU')
acronyms.remove('TUTU')
print(acronyms)

acronyms = []


acronyms = ['LOL', 'IDK', 'TOTO', 'SMH', 'TBH']
print(acronyms)

if 1 in acronyms:
    print(True)
else:
    print(False)


if 1 in [1,2,3,4,6]:
    print(True)
else:
    print(False)

word = 'IDK'
if word in acronyms:
    print("in list")
else:
    print("not in list")


print("\nExemple de boucle for :")
i=0
for acronym in acronyms:
    i = i + 1
    print(str(i) + ") " + acronym)

