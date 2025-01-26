buffer = [0] * 5
print(buffer)

index = 0
for i in range(10):
    print (index, index % len(buffer))
    buffer[index % len(buffer)] = i
    index += 1
print(buffer)