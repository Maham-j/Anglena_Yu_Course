name_1 = input ('Enter first name:')
name_2 = input ('Enter second name:')
count_1 = name_1.count('t') + name_1.count('r') + name_1.count('u') + name_1.count('e')
count_2 = name_2.count('t') + name_2.count('r') + name_2.count('u') + name_2.count('e')
count_3 = name_1.count('l') + name_1.count('o') + name_1.count('v') + name_1.count('e')
count_4 = name_2.count('l') + name_2.count('o') + name_2.count('v') + name_2.count('e')

percentage =int( str(count_1 + count_2) + str(count_3 + count_4))

if percentage <10 or percentage> '0:
    print(f'Your score is {percentage}% , you go together like coke and mentos ')
elif percentage < 50 or percentage > 40:
    print(f'Your score is {percentage}% , you are alright together ')
else:
    print(f'Your score is {percentage}%')









# Get input for the first and second names
name_1 = input('Enter first name:')
name_2 = input('Enter second name:')

# Combine the names and convert to lowercase
combined = (name_1 + name_2).lower()

# Count the occurrences of letters in "true" and "love"
true = combined.count('t') + combined.count('r') + combined.count('u') + combined.count('e')
love = combined.count('l') + combined.count('o') + combined.count('v') + combined.count('e')

# Calculate the love score by concatenating true and love counts
love_score = int(str(true) + str(love))
print(love_score)

# Determine the relationship status based on the love score
if (love_score < 10) or (love_score > 90):
    print(f'Your score is {love_score}% , you go together like coke and mentos')
elif (love_score < 50) or (love_score > 40):
    print(f'Your score is {love_score}% , you are alright together')
else:
    print(f'Your score is {love_score}%')
