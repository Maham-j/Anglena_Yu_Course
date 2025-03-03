from random import*

word_list = ['mickey','mouse','minions']
random = randint(0,2)
chosen_word = word_list[random]


guess = input()
for  letter in range(len(chosen_word)-1):
    if guess == chosen_word[letter]:
        print('right')
    else:
        print('wrong')
print('---------------------')
print(chosen_word)

















####################################
import random

word_list = ['mickey','mouse','minions']
chosen_word = random.choice(word_list)
guess = input()
for  letter in chosen_word:
    if letter == guess:
        print('yes')
    else:
        print('no')
print('---------------------')
print(chosen_word)