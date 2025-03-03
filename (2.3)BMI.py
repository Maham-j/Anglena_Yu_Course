#BMI calculator 📏🧮

height = float (input('Enter height in m: '))			# Get height in meters from the user
weight = int (input('Enter weight in kg: '))			# Get weight in kilograms from the user
BMI = weight / (height**2)					# Calculate BMI
print ('BMI:' , BMI)

if BMI < 18.5 :					# Categorize BMI
    print ('underweight')
elif BMI > 18.5 and BMI <25 :
    print ('normalweight')
elif BMI > 25 and BMI <30 :
    print ('overweight')
elif BMI > 30 and BMI< 35 :
     print ('obese')   
elif BMI > 35 :
    print ('clinically obese')
