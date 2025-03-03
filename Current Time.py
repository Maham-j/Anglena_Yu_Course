import time

# Get the current time in the format HH:MM:SS
timestamp = time.strftime('%H:%M:%S')

# Print the current timestamp
print (timestamp)

# Check the time of the day and greet accordingly
if timestamp > '0:0:0' and timestamp <='12:0:0' :
    print ('Good Morning Maham')
elif timestamp > '12:0:0' and timestamp <='15:0:0' :
    print('Good Afternoon Maham')
elif timestamp > '15:0:0' and timestamp <='20:0:0' :
    print('Good Evening Maham')
else:
    print('Good Night Maham')