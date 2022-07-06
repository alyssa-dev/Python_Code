#Using an example from the textbook, I am going to improve and change it.
users = {
 'aeinstein': {
 'first': 'albert',
 'last': 'einstein',
 'location': 'princeton',
 },
 'mcurie': {
 'first': 'marie',
 'last': 'curie',
 'location': 'paris',
 },
 'CookieC4t':{
    'first': 'Steven',
    'last': 'Universe',
    'location': 'Beach City'
 }
 }
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
    if username == 'mcurie':
        print('\tThank you for discovering radium, Marie Curie!\
        Even if you died for it.')
    elif username == 'CookieC4t':
        print('''\tOn behalf of the BLAH Organization, we would like to thank you for saving us all.''')
    else:
        print('\tNot special enough.')
    