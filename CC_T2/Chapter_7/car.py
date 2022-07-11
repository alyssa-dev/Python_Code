#I am going to request the user to input what kinda car they would like
#and then prints a reply. Keeps on going until they make a firm decision.

def choice():
    car = input('What kind of car would you like? ')
    print(f'Oh... you want a {car}?  ')

    
gamecont = True

while gamecont == True:
    choice()
    gamecont = False
    check = input('...Are you sure? ') 
    if check.lower().startswith('y'):
        print('If you say so...')
    else:
        print('Oh thank goodness...')
        gamecont = True