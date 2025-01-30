A = {10, 11, 12, 13, 14, 15, 16}
B = {13, 14, 15, 16, 17, 18, 19}

C = {12, 13}

intersection = A.intersection(B)
print(intersection)

union = A.union(B)
print(union)

subset = C.issubset(A) #C compris dans A
print(subset)

superSet = A.issuperset(C) # A contient C
print(superSet)