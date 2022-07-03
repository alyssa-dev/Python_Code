#random number game. Basically the same as the one in the textbook, but uses definitions
import random

guess = 0
number = random.randint(1, 101)

def name():
    print('What is your name? ')
    my_name = input()
    return my_name

def intro(my_name_ok):
    print('Ok, '+my_name_ok+', I will pick a number between one and one hundred. Try to guess it in six trys!')
    
def game(number):
    for guess in range(6):
        print('Guess: ')
        answer = input()
        answer = int(answer)
        if answer > number:
            print('Too high!')
        if answer < number:
            print('Too low!')
        if answer == number: 
            break
   
    if answer == number:
        print('Right! Good job '+my_name_ok+'!')
    if answer != number:
        number = str(number)
        print('It was '+number)

playagain = 'y'
while playagain == 'y' or playagain == 'Y':
    my_name_ok = name()
    intro(my_name_ok)
    game(number)
    print('Wanna play again? y or n')
    playagain = input()