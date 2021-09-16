########################################################################
##
## CS 101 Lab
## Program #2
## Nathan Bright
## nwbbdf@umsystem.edu
##
## PROBLEM : Calculating the weighted grade from a student's individual grades.
##
## ALGORITHM : 
##      1. Ask user to enter student name.
##      2. Ask user to enter student's lab, exam, and attendance grade.
##      3. Calculate entered grades into a weighted grade and letter grade.
##      4. Display the calculated grades to the user.
## 
## ERROR HANDLING:
##      Prevent user from entering grades above 100 or below 0.
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

print('---- COMP-SCI 101L Grade Calculator ----\n')

name = input('Who are we calculating grades for? ')

labGrade = int(input('\nEnter Lab grade: '))
if labGrade > 100:
    print(labGrade, 'is an invalid grade, and has been reduced to 100.')
    labGrade = 100
elif labGrade < 0:
    print(labGrade, 'is an invalid grade, and has been increased to 0.')
    labGrade = 0

examGrade = int(input('\nEnter Exam grade: '))
if examGrade > 100:
    print(examGrade, 'is an invalid grade, and has been reduced to 100.')
    examGrade = 100
elif examGrade < 0:
    print(examGrade, 'is an invalid grade, and has been increased to 0.')
    examGrade = 0

attendanceGrade = int(input('\nEnter Attendance grade: '))
if attendanceGrade > 100:
    print(attendanceGrade, 'is an invalid grade, and has been reduced to 100.')
    attendanceGrade = 100
elif attendanceGrade < 0:
    print(attendanceGrade, 'is an invalid grade, and has been increased to 0.')
    attendanceGrade = 0

weightedGrade = (labGrade * 0.7) + (examGrade * 0.2) + (attendanceGrade * 0.1)
#Ensures the weighted grade is only displayed to one decimal place.
weightedGrade2D = '{:.1f}'.format(weightedGrade)

if weightedGrade >= 90:
    letterGrade = 'A'
elif weightedGrade >= 80:
    letterGrade = 'B'
elif weightedGrade >= 70:
    letterGrade = 'C'
elif weightedGrade >= 60:
    letterGrade = 'D'
else:
    letterGrade = 'F'

print('\nThe weighted grade for', name, 'is', weightedGrade2D)
print(name, 'has a letter grade of', letterGrade, '\n')

print('--- Thank you for using the COMP-SCI 101L grade calculator! ---')
