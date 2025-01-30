import random

def dice_roll():
    dice_total = random.randint(1,6) + random.randint(1, 6)
    return dice_total

def main():
    player1 = input("Enter player 1 name:\n")
    player2 = input("Enter player 2 name:\n")

    roll1 = dice_roll()
    roll2 = dice_roll()

    print(player1, 'rolled', roll1)
    print(player2, 'rolled', roll2)

    if roll1 > roll2:
        print(player1, ' wins!')
    elif roll2 > roll1:
        print(player2, ' wins!')
    else:
        print('tie!')

main()
