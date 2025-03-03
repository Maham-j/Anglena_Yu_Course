
#First we made an empty list of diplay and then a list of words
#Then we loop through it and print blanks according to lenght of word
#Then we randomly select a word from a list of words and called it a chosen word
#and then loop through the display and input a  leter from user and if that guessed 
#letter matched any of these in chosen_word ,we replace the blank withb that word
#The input stop when no more blanks are left behind and no lives left behind
#And if the user typed incorrect word the life is decrement by 1 and print pic of hangman


_________________________________________________________________________________________________

from random import*

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']




lives = 7 
display = []
words = ['whimsical','enchanting','delightful','amusing','cheeky','cuddly','jovial','sparkling','playful','winsome']


rangee = randint(0,10)
chosen_word = words[rangee]                                             #randomly chose word from list
for _ in range (len(chosen_word)):
    display.append('_')
print(display)		                                                #a list containg blanks equal to letters in word													\

while '_' in display and  lives > 0:
    guess = input().lower()
    
    for  letter in range(len(chosen_word)):
        if chosen_word[letter] == guess:
            display[letter] = guess        
    print(display)
    
        
    if guess not in chosen_word:
        lives -= 1
        print('lives Left:',lives)
        print(HANGMANPICS[6-lives])					#as the life has been decremented by one bcz of wrong chosen word so the life is 7-1=6 and the 6-lives which is now 6 so 6-6=0 and the first index of 0th pic printed
    print('lives Left:',lives)
    
if not '_' in display :
    print('You Won')
else:
    print(f'You Lose.The word was {chosen_word}')













from random import*
from IPython.display import clear_output

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

logo = '''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                     '''




print(logo)
lives = 7
display = []
words = [
    # Animation Movies
    'frozen',
    'moana',
    'zootopia',
    'coco',
    'toystory',
    'finding nemo',
    'shrek',
    'thelionking',
    'aladdin',
    'cars',
    'mulan',
    'insideout',
    'ratatouille',
    'theincredibles',
    'kungfupanda',
    'despicable me',
    'madagascar',
    'brave',
    'pussinboots',
    
    # Fruits
    'apple',
    'banana',
    'orange',
    'grape',
    'watermelon',
    'strawberry',
    'pineapple',
    'mango',
    'cherry',
    'blueberry',
    'kiwi',
    'lemon',
    'papaya',
    'apricot',
    'pear',
    'peach',
    'plum',
    'raspberry',
    'blackberry',
    'guava',
    'cantaloupe',
    'cranberry',
    'fig',
    'date',
    'nectarine',
    'lime',
    'coconut',
    'passionfruit',
    'dragonfruit',
    'lychee',
    'pomegranate',
    'kiwifruit',
    'apricot',
    'pomelo',

    # Vegetables
    'carrot',
    'potato',
    'broccoli',
    'cucumber',
    'onion',
    'pepper',
    'tomato',
    'lettuce',
    'pumpkin',
    'cabbage',
    'cauliflower',
    'eggplant',
    'zucchini',
    'radish',
    'beetroot',
    'celery',
    'asparagus',
    'spinach',
    'artichoke',
    'sweet potato',

    # Others
    'elephant',
    'giraffe',
    'penguin',
    'koala',
    'dolphin',
    'butterfly',
    'rainbow',
    'bicycle',
    'guitar',
    'umbrella',
    'pizza',
    'chocolate',
    'sandwich',
    'umbrella',
    'suitcase',
    'television',
    'clock',
    'computer',
    'sunglasses',
    'moon',
    'raindrop',
    'starfish',
    'whale'
]


rangee = randint(0,10)
chosen_word = words[rangee]
for _ in range (len(chosen_word)):
    display.append('_')
print(display)

while '_' in display and  lives > 0:
    guess = input('Guess a word: ').lower()
    clear_output(wait=True)
    
    for  letter in range(len(chosen_word)):
        if chosen_word[letter] == guess:
            display[letter] = guess        
    print(display)
    
        
    if guess not in chosen_word:
        lives -= 1
        print(HANGMANPICS[6-lives])
    print('lives Left:',lives)
    
if not '_' in display :
    print('You Won')
else:
    print(f'You Lose.The word was {chosen_word}')
    
    
    
    S