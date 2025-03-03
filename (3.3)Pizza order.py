print('''
                                ._
                                   ,(  `-.
                                 ,': `.   `.
                               ,` *   `-.   \
                             ,'  ` :+  = `.  `.
                           ,~  (o):  .,   `.  `.
                         ,'  ; :   ,(__) x;`.  ;
                       ,'  :'  itz  ;  ; ; _,-'
                     .'O ; = _' C ; ;'_,_ ;
                   ,;  _;   ` : ;'_,-'   i'
                 ,` `;(_)  0 ; ','       :
               .';6     ; ' ,-'~
             ,' Q  ,& ;',-.'
           ,( :` ; _,-'~  ;
         ,~.`c _','
       .';^_,-' ~
     ,'_;-''
    ,,~
    i'
    :

''')
# Initialize the total bill.
total_bill = 0

# Prompt user for pizza size.
size = input ('Enter size of pizza:')

# Prompt user for pepperoni choice.
add_paperoni = input ('add_paperoni(y or n):')

# Prompt user for extra cheese choice.
extra_cheese = input('extra_cheese(y or n):')


# Calculate costs based on pizza size and toppings.
if size == 'small':
    total_bill += 15
    if add_paperoni == 'y':
        total_bill += 2

elif size == 'medium':
    total_bill += 20
    if add_paperoni == 'y':
        total_bill += 3

elif size == 'large':
    total_bill += 25
    if add_paperoni ==' y':
        total_bill += 3


# Add cost for extra cheese if chosen.
if extra_cheese == 'y':
    total_bill += 1

# Print spacing.
print()

# Display total bill.
print(f'Your total bill is:$ { total_bill }')