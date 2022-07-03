print('We are gonna do some conditional tests!')

tea = 'Tea'

if tea == 'leaf':
        print('\nLEAF me alone')
if tea != 'jwefioewj':
    print('Ready?')
if tea != 'ee':
        print('\nTHE FUNCTION IS EQUAL TO TEA MOTHERFUCKERS')


print('\nSo, first I am going to ask the code if the value "Pancake" is in it. It should say false.')
print(tea == 'pancake' )

print('\nUsing the same function, I am going to see if it has the value "Tea". Should say true.')
print(tea == 'Tea')

print('\nCool! Now I am going to lowercase one letter. Should say false')
print(tea == 'tea')

print('\nNow I am going to put the .lower() function on there. Should say true')
print(tea.lower() == 'tea')

print('\nWhat if its all in uppercase? predict false')
print(tea == 'TEA')

print('\nWhat if all in upper case with the .upper() after the function? predict true')
print(tea.upper() == 'TEA')

print('\n\nTransferring over to a list!')
list = ['lolly', 'Jig', 'Theatre']

print('\nHeres the list bitches:')
for value in list:
    if value == 'Jig':
        print(value.upper())
    else:
        print(value.title())

print('\ngonna see if yellow is in there. Should say false')
print('yellow' in list)

print('\nGonna see if Jig is in there. Should be true')
print('Jig' in list)

print('\n\nNUMBERS TIME BITCHES')
jig = 4
me = 18

print('\ngonna ask if jig >= 18 or me >= 18. TRUE BECAUSE IM EIGHTEEN AND OLDER FOOLS')
print(jig >= 18 or me >= 18)

print('\nSAME THING BUT NOW ITS GONNA BE FALSE CAUSE IT WILL BE jig >= 18 and me >= 18')
print(jig >= 18 and me >= 18)

if jig != 18:
    print('JIG IS NOT EIGHTEEN')