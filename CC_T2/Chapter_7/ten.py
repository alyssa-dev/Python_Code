#The program will tell if a number inputted it a mutliple of ten 

number = input('Tell me a number and I will let you know if it is multiple of ten: ')
number = int(number)

if number % 10 == 0:
    print(f'{number} is a multiple of ten')
else:
    print(f'{number} is not a multiple of ten')
