#after studying the og code, I made this from memory.
#REMEMBER THAT INT AND STR ARE NOT COMPATABLE
import random
import time

print('coins, 1000, head, how many? press enter to start')
input()

flips = 0
heads = 0

while flips < 1000:
    if random.randint(0, 1) == 1:
        heads = heads + 1
    flips = flips + 1
    
    if flips == 100:
        print('100 flips, ' +str(heads)+' heads.')
        time.sleep(1)
    if flips == 500:
        print('halfway, '+str(heads)+ ' heads.')
        time.sleep(1)

print('\n finished, ' +str(heads)+ ' heads')