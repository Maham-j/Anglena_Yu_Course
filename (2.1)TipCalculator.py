# This program calculates the amount each person needs to pay, including a tip, based on the total bill and the number of people.
#Tip Calculator

total_bill = float(input('Enter total bill? Rs.'))                     # Get input from the user
people = int(input('Enter total people:'))
tip = int(input('how much you want to give?%'))

amount_per_person = round((total_bill/people) * ((tip/100)+1))         # Calculate the amount each person needs to pay, including the tip
print("amount_per_person:Rs.", amount_per_person)                      # Display the calculated amount per person