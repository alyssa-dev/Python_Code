my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

friend_foods.append('Lemon')
friend_foods.sort()

print("My favorite:".title())
for blah in my_foods[:]:
    print(blah.title())
print("\nfriends favorite:".title())
for meh in friend_foods[:]:
    print(meh.title())
