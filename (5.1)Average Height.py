#############################################################
student_heights = input( 'Input a list of student heights').split()

for n in range (0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

sum = 0
for i in student_heights:
    sum +=i

no_of_students = 0
for j in student_heights:
    no_of_students += 1
print('No_of_students:',no_of_students)

Ave = sum/no_of_students
print('Ave:',round(Ave))













################################################S
student_heights = input('Input a list of student heights').split()
sum=0 
for n in range (0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    sum += student_heights[n]
    
print(student_heights)
Ave = sum/len(student_heights)
print('Average:',round(Ave))