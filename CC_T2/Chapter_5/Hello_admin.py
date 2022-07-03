usernames = ['admin', 'John Doe', 'Jane Doe', 'Franklin', 'Bob']


if usernames:
    for username in usernames:
        if username == 'admin':
            print('Welcome, ' +username.title()+', would you like a status report?')
        
        else:
            print('Welcome, ' +username.title()+', thanks for logging on!')

else:
    print('We need some peeps in here.')