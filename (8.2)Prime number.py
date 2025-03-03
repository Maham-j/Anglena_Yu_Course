def prime_no(number):
    is_prime = True
    for i in range(2,number):
        if number % i ==0:
            is_prime = False
    if is_prime:
        print('Its prime')
    else:
        print('Its not prime')
prime_no(75)    












###############################
def prime_no(number):
    for i in range(2,number):
        if number %i ==0:
            print('its not prime')
    print('its prime')
prime_no(75)