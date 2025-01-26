# game loop
while True:
    mountain_chain = dict()
    for i in range(5):
        mountain_h = int(input())
        mountain_chain.update({i : mountain_h})
    
    mountain = max(mountain_chain, key=mountain_chain.get)
    print('\nK:', mountain, 'V:', mountain_chain.get(mountain))

