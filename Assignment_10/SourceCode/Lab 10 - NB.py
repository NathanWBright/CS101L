########################################################################
##
## CS 101 Lab
## Program 10
## Nathan Bright
## nwbbdf@umsystem.edu
##
## PROBLEM: We need to display the most common words and their frequencies to a text file entered by a user.
##
## ALGORITHM: 
##      1. Ask the user to enter a file and assign the contents of the file to a variable.
##      2. Remove words that are shorter than 3 letters.
##      3. Count how many times each word occurs in the file.
##      4. Sort the words in order.
##      5. Display the top 10 most common words, as well as how many unique words there are and how many words only occurred once.
## 
## ERROR HANDLING:
##      1. FileNotFoundError for if the user enters a file that doesn't exist
##      2. IOError for if the user enters an invalid file.
##      
## OTHER COMMENTS:
##      
##
########################################################################

def open_file(prompt, mode = 'r'):
# Attempts to open the users desired file. If the file is invalid, tells the user and asks them to enter a different one.
    while True:
        try:
            filename = input(prompt)
            file = open(filename, mode)
            return file
        except FileNotFoundError:
            print('Could not open file', filename)
        except IOError:
            print('IO Error attempting to open', filename)

def remove_short_words(text):
# Gets rid of punctuation, capitalization, and elements that may mess with our data, and removes any word that is less than 4 characters long.
    valid_words = []
    text = text.replace('.','')
    text = text.replace(',','')
    text = text.replace('!','')
    text = text.replace('?','')
    text = text.lower()
    text = text.split()
    for word in text:
        if len(word) > 3:
            valid_words.append(word)
    return valid_words

def word_count(words):
# Processes all of the words to give us a dict for each word with the number of times it occurs.
    occurences = {}
    for word in words:
        if word in occurences:
            occurences[word] += 1
        else:
            occurences[word] = 1
    return occurences

def text_sorting(text):
# Sorts the words in order of occurence.
    sorted_text = dict(reversed(sorted(text.items(), key = lambda kv: kv[1])))
    return sorted_text

def display_results(result):
# Displays the results in a clean and easily readable format.
    format = '{num:<6}{word:>12}{freq:>8}'
    lines = 0
    instances_one = 0
    print(format.format(num='#', word='Word', freq='Freq'))
    print('=' * 26)
    for key, value in result.items():
        if lines < 10:
            lines += 1
            print(format.format(num=lines, word=key, freq=value))
        if value == 1:
            instances_one += 1

    print('\nThere are', instances_one, 'words that occur only once.')
    print('There are', len(result), 'unique words in the document.')

if __name__ in '__main__':
    prompt = 'Please enter a text file ==> '

    file = open_file(prompt)
    text = file.read()
    file.close()

    sorted_text = text_sorting(word_count(remove_short_words(text)))
    display_results(sorted_text)