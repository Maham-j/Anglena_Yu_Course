#So that programs do not cause error and take only valid input

data_valid = False

while data_valid == False:
     grade = input()
    try:
        grade = float(grade)
    except:
        print ('Invalid')
        continue
        
    if grade < 0 or grade > 10:
        print('Grade should be between 0 and 10')
	continue

    else:
        data_valid = True
print("Invalid input. Please enter a valid number.")

