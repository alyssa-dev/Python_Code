#Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. 
#Use a for loop to print each number.

odd_numbers = []
for oddies in range(1, 20, 2):
    odd_numbers.append(oddies)

print(odd_numbers)