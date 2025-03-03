import random
colors = ['blue','pink','yellow','red','green','orange','white','black','brown']
while True:
    guess = input ('Enter your guess: ')
    color = random.choice(colors)
    
    if guess == color:
        print ('Congrats.You won')
        break
    else:
        print('you loose')
        
    again = input('Wanna play again? Y or N').upper()
    if again == 'N':
        print (f'Thanks for playing!.The color was {color}.')
        break
