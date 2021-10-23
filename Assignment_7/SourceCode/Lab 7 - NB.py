########################################################################
##
## CS 101 Lab
## Program 7
## Nathan Bright
## nwbbdf@umsystem.edu
##
## PROBLEM : Take a list of vehicles and give the user a file with only the vehicles above a desired MPG
##
## ALGORITHM : 
##      1. Ask the user for a desired MPG of car.
##      2. Ask the user for a vehicle file to read.
##      3. Attempts to convert vehicle file values into something the rest of the program can read.
##      4. Ask the user for a file to write the filtered car information to.
##      5. Print a list of cars with more than the desired MPG to the users desired file.
## 
## ERROR HANDLING:
##      1. ValueError prevention for integer conversions
##      2. FileNotFoundError handling for trying to open files.
##      3. IOError handling for trying to read or write to files.
##      
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

def valid_mpg():
# Asks the user to enter a minimum MPG between 0 and 100. If they enter anything else ask them to enter again. 
    while True:
        try:
            minmpg = int(input('Enter the desired minimum MPG ==> '))
            if minmpg > 100:
                print('Fuel economy must be less than 100 MPG.')
                continue
            elif minmpg < 0:
                print('Fuel economy must be greater than 0 MPG.')
                continue
            else:
                return minmpg
        except ValueError:
            print('You must enter a number to represent your desired fuel economy.')

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

def check_write_file(prompt, mode = 'w'):
# Attempts to write to the users desired file. If the file is invalid, tells the user and asks them to enter a different one.
    while True:
        try:
            filename = input(prompt)
            file = open(filename, mode)
            return file
        except IOError:
            print('IO Error attempting to write to', filename)

def process_file():
# Converts the contents of the original file to only have the information we want to give the user, and cleans up the formatting for the code to more easily work with.
    comprehensivelist = []
    vehiclelist = vehicles.splitlines()
    for ln in vehiclelist:
        newln = ln.split('\t')
        newlist = []
        newlist.append(newln[0])
        newlist.append(newln[1])
        newlist.append(newln[2])
        newlist.append(newln[-3])
        comprehensivelist.append(newlist)
    del comprehensivelist[0]

    final_list = []
    for ln in comprehensivelist:
        try:
            if int(ln[3]) >= minmpg:
                final_list.append(ln)
                continue
            else:
                continue
        except ValueError:
            print('Can not convert value', ln[3], 'for vehicle', ln[0:2])
            continue
    return final_list

def write_file(file):
# Prints out the processed file, formatted.
    format_string = '{name:<40}{mpg:>10}'
    for grp in final_list:
        combinedtxt = grp[0] + ' ' + grp[1] + ' ' + grp[2]
        temptxt = format_string.format(name=combinedtxt, mpg=grp[3])
        temptxt += '\n'
        file.write(temptxt)

# Defines for prompts used to ask users to input files.
prompt = 'Enter the name of the input vehicle file ==> '
secondprompt = 'Enter the name of the file you wish to output to ==> '

# Asks user for a desired MPG.
minmpg = valid_mpg()

# Opens and closes file.
file = open_file(prompt)
vehicles = file.read()
file.close()

# Defines a fully processed file as final_list.
final_list = process_file()

# Attempts to write our processed file.
file_to_write = check_write_file(secondprompt)
write_file(file_to_write)
file_to_write.close()
