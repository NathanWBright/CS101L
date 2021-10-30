########################################################################
##
## CS 101 Lab
## Program 8
## Nathan Bright
## nwbbdf@umsystem.edu
##
## PROBLEM: We want to allow a user to add and remove grades, and display them with additional information and a weighted grade.
##
## ALGORITHM: 
##      1. Allow the user to select an option for the menu.
##      2. Handle being able to add and remove elements from a list.
##      3. Handle being able to calculate the mean and stdev of tests and assignments.
##      4. Display scores to the user.
## 
## ERROR HANDLING:
##      1. Prevents divide by zero error when dealing with mean and stdev calculations.
##      2. Value Error prevention throughout.
##      
## OTHER COMMENTS:
##
##
########################################################################

import math

#Universal Defines
running = True
tests = []
assignments = []

def grade_menu():
    #Gives user a selection of options to pick from.
    print('\nGrade Menu')
    print('1 - Add Test')
    print('2 - Remove Test')
    print('3 - Clear Tests')
    print('4 - Add Assignment')
    print('5 - Remove Assignment')
    print('6 - Clear Assignments')
    print('D - Display Scores')
    print('Q - Quit')

def menu_selection():
    #Handles the user selecting an option from the menu.
    global running
    while True:
        selection = input('\n==> ')
        if selection == '1':
            add_test()
            break
        elif selection == '2':
            remove_test()
            break
        elif selection == '3':
            clear_test()
            break
        elif selection == '4':
            add_assignment()
            break
        elif selection == '5':
            remove_assignment()
            break
        elif selection == '6':
            clear_assignments()
            break
        elif selection == 'D' or selection == 'd':
            display_score()
            break
        elif selection == 'Q' or selection == 'q':
            running = False
            break
        else:
            print('Please enter a valid selection.')
            continue

def add_test():
    #Appends a score to the list of tests.
    test = score_validity('test')
    tests.append(test)

def remove_test():
    #Removes a score from the list of tests.
    try:
        test = can_remove_score('test')
        tests.remove(test)
    except ValueError:
        print('Could not find that score to remove.')

def clear_test():
    #Removes all elements from list of tests.
    tests.clear()

def add_assignment():
    #Appends a score to the list of assignments.
    assignment = score_validity('assignment')
    assignments.append(assignment)

def remove_assignment():
    #Removes a score from the list of assignments.
    try:
        assignment = can_remove_score('assignment')
        assignments.remove(assignment)
    except ValueError:
        print('Could not find that score to remove.')

def clear_assignments():
    #Removes all elements from list of assignments.
    assignments.clear()

def display_score():
    #Prints out various calculated attributes of tests and assignments in a readable format.
    str_format = '{type:<20}{num:>8}{min:>8}{max:>8}{avg:>8}{std:>8}'
    score_format = '{type:<20}{num:>8}{min:>8.1f}{max:>8.1f}{avg:>8.2f}{std:>8.2f}'

    print(str_format.format(type='Type', num='#', min='min', max='max', avg='avg', std='std'))
    print('=' * 60)

    if tests == []: #If the list is empty, override the values with n/a.
        print(str_format.format(type='Tests', num='0', min='n/a', max='n/a', avg='n/a', std='n/a'))
    else:
        print(score_format.format(type='Tests', num=len(tests), min=min(tests), max=max(tests), avg=mean_calculation(tests), std=stdev_calculation(tests, mean_calculation(tests))))
    if assignments == []: #If the list is empty, override the values with n/a.
        print(str_format.format(type='Assignments', num='0', min='n/a', max='n/a', avg='n/a', std='n/a'))
    else:
        print(score_format.format(type='Assignments', num=len(assignments), min=min(assignments), max=max(assignments), avg=mean_calculation(assignments), std=stdev_calculation(assignments, mean_calculation(assignments))))

    print('\nThe weighted score is: {:.2f}'.format(score_weighted(mean_calculation(tests), mean_calculation(assignments))))

def score_validity(score_type):
    #Ensures that any value to be added is valid.
    while True:
        try:
            score = float(input('Enter the new {} score 0-100 ==> '.format(score_type)))
            if score < 0:
                print('The score you entered was above zero. Please enter a value above zero.')
            else:
                break
        except ValueError:
            print('You must enter a float value for the score.')
    return score

def can_remove_score(score_type):
    #Checks if the score the user wants to remove is a float.
    while True:
        try:
            score = float(input('Enter the {} score to remove ==> '.format(score_type)))
            break
        except ValueError:
            print('Could not find that score to remove.')
    return score

def mean_calculation(scores):
    #Calculates mean of all scores inside of tests or assignments.
    total_score = 0
    for score in scores:
        total_score += score
    if len(scores) == 0: #Prevents divide by zero errors.
        return 0
    avg_score = total_score / len(scores)
    return avg_score

def stdev_calculation(scores, score_avg):
    #Calculates standard deviation of all scores inside of tests or assignments.
    numerator = 0
    for score in scores:
        numerator += ((score - score_avg) ** 2)
    if len(scores) == 0: #Prevents divide by zero errors.
        return 0
    stdev = math.sqrt(numerator / len(scores))
    return stdev

def score_weighted(avg_score1, avg_score2):
    #Returns a weighted score with the first score being with 60% and the second being with 40%.
    weighted = (avg_score1 * 0.6) + (avg_score2 * 0.4)
    return weighted

while running == True:
    #Main program, just handles the menu where most other functions are called.
    grade_menu()
    menu_selection()
