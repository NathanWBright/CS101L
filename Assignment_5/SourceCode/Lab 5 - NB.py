########################################################################
##
## CS 101 Lab
## Program 5
## Nathan Bright
## nwbbdf@umsystem.edu
##
## PROBLEM : Checking Library Card IDs
##
## ALGORITHM : 
##      1. Ask the user to enter a library card string
##      2. Check the length of the string to ensure it is 10 characters long
##      3. Check for valid characters within the string
##      4. Run a check digit to ensure the card value is valid.
##      5. Tell the user information about the card holder.
## 
## ERROR HANDLING:
##      1. Prevents user from entering an invalid card number.
##      2. Prevents user from entering digits where there should be letters and vice versa.
##      
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

import string
check_digit = 0

def character_value(char : str) -> int:
    char_value = string.ascii_uppercase.index(char)
    return char_value

def get_check_digit(idnumber : str) -> int:
    ''' Returns the check digit for the name and sid. '''
    global check_digit
    check_digit = 0
    index_no = 0
    idlist = list(idnumber)
    for i in idlist:
        if index_no <= 4:
            check_digit += character_value(i) * (index_no + 1)
            index_no += 1
        elif index_no >= 5 and index_no <= 8:
            check_digit += int(i) * (index_no + 1)
            index_no += 1
    check_digit = check_digit % 10
    return check_digit

def verify_check_digit(idnumber : str) -> tuple:
    ''' returns True if the check digit is valid, False if not '''
    if len(idnumber) != 10:
        return False, "The length of the number given must be 10"
    idlist = list(idnumber)
    index_no = 0
    for i in idlist:
        if i.isupper() == False and index_no <= 4:
            return False, "The first 5 characters must be A-Z, the invalid character at index {} is {}".format(index_no, i)
        elif i.isdigit() == False and index_no >= 7:
            return False, "The last 3 characters must be 0-9, the invalid character at index {} is {}".format(index_no, i)
        else:
            index_no += 1
            continue
    if idlist[5] != '1' and idlist[5] != '2' and idlist[5] != '3':
        return False, "The sixth character must be 1 2 or 3"
    if idlist[6] != '1' and idlist[6] != '2' and idlist[6] != '3' and idlist[6] != '4':
        return False, "The seventh character must be 1 2 3 or 4"
    if int(idlist[9]) != get_check_digit(idnumber):
        return False, "Check digit {} does not match calculated value {}.".format(idlist[9], check_digit)
    return True, ""

def get_school(idnumber : str) -> str:
    ''' Returns the school the 5th index or 6th character is for. '''
    idlist = list(idnumber)
    if idlist[5] == '1':
        return "School of Computing and Engineering SCE"
    elif idlist[5] == '2':
        return "School of Law"
    elif idlist[5] == '3':
        return "College of Arts and Sciences"
    else:
        return "Invalid School"

def get_grade(idnumber : str) -> str:
    '''Returns the grade for index 6'''
    idlist = list(idnumber)
    if idlist[6] == '1':
        return "Freshman"
    elif idlist[6] == '2':
        return "Sophomore"
    elif idlist[6] == '3':
        return "Junior"
    elif idlist[6] == '4':
        return "Senior"
    else:
        return "Invalid Grade"

if __name__ == "__main__":

    print("{:^60}".format("Linda Hall"))
    print("{:^60}".format("Library Card Check"))
    print("="*60)

    while True:

        print()
        card_num = input("Enter Libary Card.  Hit Enter to Exit ==> ").upper().strip()
        if card_num == "":
            break
        result, error = verify_check_digit(card_num)
        if result == True:
            print("Library card is valid.")
            print("The card belongs to a student in the {}".format(get_school(card_num)))
            print("The card belongs to a {}".format(get_grade(card_num)))
        else:
            print("Libary card is invalid.")
            print(error)
        