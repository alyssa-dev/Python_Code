#asks guests how many people will be joining them and if number is more than eight
#tells them they will have to wait. It will also repeat until a number is inputed

guests = input('How many people will be seated at this fine restraunt? ')

while guests not in '1234567890':
    print('Please enter a number')
    guests = input('How many people will be seated at this fine restraunt? ')

if int(guests) >= 8:
    print('Sorry, there will be a two hundred minute wait.')
elif int(guests) < 8:
    print('Please, follow me.')
