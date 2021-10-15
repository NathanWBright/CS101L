########################################################################
##
## CS 101 Lab
## Program 6
## Nathan Bright
## nwbbdf@umsystem.edu
##
## PROBLEM : Encode and Decode a Cypher by shifting alphabet by a given amount.
##
## ALGORITHM : 
##      1. Ask user whether or not they wish to encode, decode, or quit.
##      2. Ask user for a phrase to encode or decode, and how many characters they'd like to shift the phrase.
##      3. Process every single letter of the phrase and shift it.
##      4. Join every processed letter into a complete string.
##      5. Output string to user.
## 
## ERROR HANDLING:
##      1. Prevents user from entering an invalid value when asked how much they'd like to shift letters
##      2. Forces letters to loop back to the beginning (or end) of the alphabet if they'd otherwise shift to a non letter character.
##      3. If the user enters something that isn't a letter into the string, the program just ignores it to prevent unwanted behavior.
##      
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

import string

def encode(text, shift):
    '''Caesar-encrypts string using specified key.'''
    encoded_text = []
    for i in text:
        '''We don't want to encode spaces'''
        if i == ' ':
            encoded_text.append(i)
            continue
        '''If an invalid character is entered, ignore it and process everything else'''
        if i.isalpha() == False and i != ' ':
            continue
        text_value = ord(i.upper())
        '''Ensures that a letter loops to the beginning or end of the alphabet. Capital letters between 65 and 91 (Inclusive)'''
        if text_value + shift >= 91:
            text_value -= 26
        if text_value + shift <= 64:
            text_value += 26
        encoded_chr = chr(text_value + shift)
        encoded_text.append(encoded_chr)
    '''Returns list as a sanitized string.'''
    encoded_text = ''.join(encoded_text)
    encoded_text = encoded_text.replace('#', ' ')
    return encoded_text

def decode(text, shift):
    ''' Decrypts Caesar-encrypted string with specified key.'''
    decoded_text = []
    for i in text:
        '''We don't need1 to decode spaces'''
        if i == ' ':
            decoded_text.append(i)
            continue
        '''If an invalid character is entered, ignore it and process everything else'''
        if i.isalpha() == False and i != ' ':
            continue
        text_value = ord(i.upper())
        '''Ensures that a letter loops to the beginning or end of the alphabet. Capital between 65 and 91 (Inclusive)'''
        if text_value - shift >= 91:
            text_value -= 26
        if text_value - shift <= 64:
            text_value += 26
        decoded_chr = chr(text_value - shift)
        decoded_text.append(decoded_chr)
    '''Returns list as a sanitized string.'''
    decoded_text = ''.join(decoded_text)
    decoded_text = decoded_text.replace('#', ' ')
    return decoded_text

def get_input():
    '''Seperates out initial user input.'''
    user_input = input('Enter your selection ==> ')
    return user_input

def print_menu():
    '''Prints out the menu.'''
    print('\nMAIN MENU:')
    print('1) Encode a string')
    print('2) Decode a string')
    print('Q) Quit')

while True:
    print_menu()
    userRequest = get_input()
    if userRequest == '1':
        encodetxt = input('\nEnter brief text to encrypt: ')
        try:
            shiftamt1 = int(input('Enter how many characters you wish to shift to the letters: '))
        except ValueError:
            print('Error: You must enter a numerical value to shift the letters. Please try again.')
            continue
        encoded_result = encode(encodetxt, shiftamt1)
        print(encoded_result)
    if userRequest == '2':
        decodetxt = input('\nEnter brief text to decrypt: ')
        try:
            shiftamt2 = int(input('Enter how many characters you wish to shift to the letters: '))
        except ValueError:
            print('Error: You must enter a numerical value to shift the letters. Please try again.')
            continue
        decoded_result = decode(decodetxt, shiftamt2)
        print(decoded_result)
    if userRequest == 'Q':
        break
    if userRequest != '1' and userRequest != '2' and userRequest != 'Q':
        print('Please enter a valid response')
