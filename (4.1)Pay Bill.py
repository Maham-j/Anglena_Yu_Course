################################################################(by using indexes)

from random import*

names = ['maham','zeenat','ahsan','iqra','faiza','usama']
index = randint(0,len(names))
print(f'{names[index].capitalize()} is going to buy the meal today!')










########################################################################(incase if u wanna input the list(split is used for making list of the input taken by user separated by comma))

name = input('')
names = name.split(',')
index = randint(0,5)
print()
print(f'{names[index].capitalize()} is going to buy the meal today!')








#########################################################################(by using choice function)

import random

# List of names
name = input('Input names separated by comma: ')
names = name.split(',')

# Randomly select a name from the list
selected_name = random.choice(names)

# Print the selected name with capitalization
print(f'{selected_name.capitalize()} is going to buy the meal today!')