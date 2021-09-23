########################################################################
##
## CS 101 Lab
## Program 3
## Nathan Bright
## nwbbdf@umsystem.edu
##
## PROBLEM : We need to guess the number a user is thinking of based on the
##           remainder when we divide by 3, 5, and 7.
##
## ALGORITHM : 
##      1. Ask for the user to think of a number between 1 and 100.
##      2. Ask the user what the remainder of the number is if divided by 3, 5, and 7.
##      3. Check through all valid numbers and find the one that has the same remainders that the user entered.
##      4. Display the number the matches what the user was thinking of.
##      5. Ask if the user would like to keep playing, or quit.
## 
## ERROR HANDLING:
##      Checks for when the user enters a negative of excessive value as a remainder.
##      If the guesser cannot find a matching number, it informs the user and restarts the program.
##      Checks to ensure the user enters a valid string during the restart prompt. Asks them to enter a string again if it's not.
##
## OTHER COMMENTS:
##      if statements don't like "variable == 'X' or 'Y'"" and it breaks things. Do "variable == 'X' or variable == 'Y'" instead.
##
########################################################################

play = True
# Asks user to enter the remainder of a number when it is divided by a code designated amount.
# Checks if the entered number is valid, and returns it if so.
def remainderQ(divis_by):
    divis_num = int(input('\nWhat is the remainder of your number when it is divided by {}? '.format(divis_by)))
    if divis_num < 0:
        print('The value entered must be greater than or equal to 0.')
        remainderQ(divis_by)
    elif divis_num >= divis_by:
        print('The value entered must be less than {}.'.format(divis_by))
        remainderQ(divis_by)
    else:
        return divis_num

# Asks the user if they would like to play again, and asks again if an invalid value is asked.
def playagainQ():
    global playagain
    replay = input('\nWould you like to play again? Y to continue, N to quit ==> ')
    if replay == 'Y' or replay == 'y' or replay == 'N' or replay == 'n':
        playagain = replay
        return
    else:
        playagainQ()

print('Welcome to the Flarsheim Guesser.')
# Asks user to think of a number between 1 and 100.
# Asks the user for the remainder when number is divided by 3, 5, or 7.
while play:
    print('\nPlease think of a number between and including 1 and 100.')
    remainder_3 = remainderQ(3)
    remainder_5 = remainderQ(5)
    remainder_7 = remainderQ(7)
    # Attempts to divide every number between 0 and 100 by 3, 5, and 7 until one number matches every user-entered value.
    for num in range(1, 101):
        if num % 3 == remainder_3 and num % 5 == remainder_5 and num % 7 == remainder_7:
            user_num = num
            break
        else: #If no valid number was found, breaks the loop.
            if num == 100:
                print('\nUnable to find your number, please ensure it is between 1 and 100.')
                user_num = 'invalid'
                break
            else:
                continue
    if user_num == 'invalid':
        continue
    # Displays the result.
    print('\nYour number was', user_num, '\nHow amazing is that?')
    # Asks the user if they would like to play again, and asks again if an invalid value is asked.
    playagainQ()
    # If yes, restart program, otherwise end.
    if playagain == 'Y' or playagain == 'y':
        continue
    else:
        break
