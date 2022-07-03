#This is used as an example on how to find bugs within code
import random
number1 = random.randint(1, 10)
number2 = random.randint(1, 10)
print('What is '  + str(number1) + ' + ' + str(number2) + '?')
answer = input()
if answer == number1 + number2: #a string and int cannot be equal.
                                #it should be: int(answer) = number1 + number2
    print('Correct!')
else:
    print('Nope! The answer is ' + str(number1 + number2))

