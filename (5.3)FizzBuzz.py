# Loop through numbers from 1 to 100 (inclusive)
for i in range (1,101):

# Print 'FizzBuzz' if divisible by both 3 and 5
    if i%5 == 0 and i%3 == 0:
        print('FizzBuzz')

# Print 'Fizz' if divisible by 3
    elif i%3 == 0:
	print('Fizz')
# Print 'Buzz' if divisible by 5
    elif i%5 ==0:
	print('Buzz')

# Print the number if it's not divisible by 3 or 5   
    else:
        print(i)