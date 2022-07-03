#this is a program using every function learned in chapter three so far, so... it's a lotta functions

books = ['project hail mary','call me daddy','public sex','algorithms']

print(f"This is what the list looks like with zero tampering")
print(books)

print("\nNow I will be putting it into reverse order")
books.reverse()
print(books)

print("\nNow I am putting it into reverse alphabetical order")
print(sorted(books ,reverse=True))

print("\nNow I am going to put it permanetly into aplhabetical order")
books.sort()
print(books)

print("\nIt\'s time to get funky by popping an item out. Also,random things will be in title mode from here on out.")
loser = books.pop(3)
print(f"{loser.title()} has left")
print(books)

print("\nI am going to remove another item but keep it accesable")
uh_oh = 'call me daddy'
books.remove(uh_oh)
print(f"{uh_oh.title()} has left")
print(books)

print("\nI\'m gonna insert public sex back in there")
books.insert(2, loser.title())
#could also use the value instead of a function
print(books)

print("\nI\'m gonna add something to the end there")
here = 'lord of the rings'
books.append(here.title())
print(books)

print("\nGoing to replace that one with another one")
books[3] = uh_oh.title()
#again, could be a value, i just used a function
print(books)

print("\nI am going to delete one of the values now")
del books[3]
print(books)

print("\nNow I\'m gonna print the last item in the list")
print(books[-1])

print("\nFinally, I am going to print how much are left in the list:")
print(len(books))