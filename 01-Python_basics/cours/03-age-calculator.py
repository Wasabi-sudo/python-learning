age = int(input("How old are you?\n"))

decades = age // 10
years = age % 10

print("You are " + str(decades) + " decades and " + str(years) + " years old.")


print("37 / 10 = " + str(37/10))
print("37 // 10 = " + str(37//10))
print("37 % 10 = " + str(37%10))

# les opérations // et % de Python ne coïncident avec la division
#euclidienne que lorsque le diviseur est positif. Lorsqu’il est négatif, le
#reste est alors également négatif.

#           a = 7   a = −7  a = 7   a = −7
#           b = 3   b = 3   b = −3  b = −3
#a // b     2       −3      −3      2
#a % b      1       2       −2      −1