pet_1 = {'Name': 'Jig', 'Species' : 'Cockatiel', 'Owner' : 'Alyssa Smith'}
pet_2 = {'Name': 'Maxx', 'Species' : 'Dog', 'Owner' : 'Joshua Smith'}
pet_3 = {'Name': 'Bella', 'Species' : 'Dog', 'Owner' : 'Joshua Smith'}
pet_4 = {'Name': 'Rocko', 'Species' : 'Rock', 'Owner' : 'Zoey'}

pets = [pet_1, pet_2, pet_3, pet_4]

for pet in pets:
    name = pets['Name']
    Species = pet['Species']
    Owner = pet['Owner']

    print(f'Name: {name}')
    print(f'Species: {Species}')
    print(f'Owner: {Owner}')

#FIX THIS CODE!!!! It doesn't work.