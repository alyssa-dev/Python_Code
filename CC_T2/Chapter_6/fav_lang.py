favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

should = ('jen','edward','lactose','jeff','philip')

for person in favorite_languages.keys():
    if person in should:
        print(f'Thank you for taking the poll, {person.title()}!')
    else:
        print(f'Hey, {person.title()}, you should take the poll or else I will murder you!')