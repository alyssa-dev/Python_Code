import random
import time

def displayIntro():
    print('''\tYou are in a land full of dragons. In front of you, you see
    you see three caves. In one cave, the dragon is friendly
    and will share his treasure with you. The other dragon
    is greedy and hungry, and will eat you on sight.
    The other other dragon will become obsessively in love with you.\n''')


def chooseCave():
    cave = ''
    while cave !='1' and cave !='3' and cave !='2':
        cave = input('Which cave will you go into? (1, 2, or 3)\n')
    return cave

def checkCave(chosenCave):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! They opens their jaw and...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 3)
    lover_dragon = random.randint(1,3)

    if chosenCave == str(friendlyCave):
        print('Gives you their treasure!')
    elif chosenCave == str(lover_dragon):
        print('Fall in love with you. They fallow you around the world, serenading you, giving gifts, until you explode from frustration.')
    else:
        print('Gobbles you down in one bite!')

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)
    print('Do you want to play again? (yes or no)')
    playAgain = input() 
    
