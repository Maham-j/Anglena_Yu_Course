# Get user's age as input
Age = int(input("What is your age?\n"))

# Calculate remaining years until 90 years old.
age = 90-Age

# Calculate days, weeks, and months based on remaining years.
days = (age*365)
weeks = (age*52)
months = (age*12)

# Display the calculated time spans.
print(f"you have {days} days , {weeks} weeks and {months} months in your life!" )