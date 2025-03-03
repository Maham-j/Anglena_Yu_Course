#############################################

student_scores = {
    'Haryy':81,
    'Ron':78,
    'Hermione':99,
    'Draco':74,
    'Neville':62,
}
student_grades = {}
for key in student_scores:
    if student_scores[key] > 90:
        grade = 'Outstanding'
    elif student_scores[key] > 80 :
        grade = 'Exceeds Expectations'
    elif student_scores[key] > 70:
        grade = 'Acceptable'
    elif student_scores[key] < 70:
        grade = 'Fail'
    student_grades[key] = grade
print(student_grades)







#######################################
student_scores = {
    'Haryy':81,
    'Ron':78,
    'Hermione':99,
    'Draco':74,
    'Neville':62,
}
student_grades = {}
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = 'Outstanding'
    elif score > 80 :
        student_grades[student] = 'Exceeds Expectations'
    elif score > 70:
        student_grades[student] = 'Acceptable'
    elif score < 70:
        student_grades[student] = 'Fail'

print(student_grades)
