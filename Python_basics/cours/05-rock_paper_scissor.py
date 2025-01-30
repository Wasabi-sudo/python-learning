import random

ia_choice = random.choice(['rock', 'paper', 'scissors'])
user_choice = input('Do you want rock, paper or scissors ?')

print('IA choice :' + ia_choice)

if ia_choice == user_choice:
    print('Egalité')
elif user_choice == 'rock' and ia_choice == 'scissors':
    print('You win')
elif user_choice == 'paper' and ia_choice == 'rock':
    print('You win')
elif user_choice == 'scissors' and ia_choice == 'paper':
    print('You win')
else:
    print('You looose')