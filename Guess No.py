from random import*
number = randint (0,10)
guess = int(input('Guess number:'))
while True:
    if number == guess:
        break
        
    else:
        guess = int(input('Nope.Try gain'))
print ('You guessed.I was thinking about numer',number)







# TO PRINT RANDOM PEOPLE

import random
people = []
for names in range (0,8):
    name = input()
    people.append (name)
index = randint (0,7)
random = people [index]
print ('Random person is :', random