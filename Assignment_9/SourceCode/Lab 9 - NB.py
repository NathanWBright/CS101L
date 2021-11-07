########################################################################
##
## CS 101 Lab
## Program 9
## Nathan Bright
## nwbbdf@umsystem.edu
##
## PROBLEM: We need to read from a CSV file and be able to display to the user the info contained in the CSV file in a digestible format.
##
## ALGORITHM: 
##      1. Open a CSV file given by the user.
##      2. Sort out dates and crime frequency from the information contained in the file.
##      3. Sort out months and crime frequency from the information contained in the file.
##      4. Convert numerical months into the names of those months.
##      5. Sort out crimes and frequency from the information contained in the file.
##      6. Display the sorted information to the user.
##      7. Display information on crimes based on zip codes on the crime that user requested.
## 
## ERROR HANDLING:
##      1. ValueError handling for if the csv file contains an invalid number as the date.
##      2. FileNotFoundError handling for when a file does not exist.
##      3. IOError handling for if attempting to open a file causes an IOError.
##      
## OTHER COMMENTS:
##      create_offense_by_zip gave me a ton of trouble, and while I am sure it's simple, I could not figure out how to properly do what is needed for the function.
##
########################################################################

import csv

def month_from_number(number):
    #Converts the numerical month of the date in which a crime occured to the name of the month.
    months = {'01':'January', '02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'December'}
    try:
        return months[number]
    except ValueError:
        print('Error: Detected number not within 1 and 12.')

def read_in_file(filename):
    #Returns the csv file entered previously as a value the rest of the program can work off of.
    csv_file = csv.reader(filename)
    reports = []
    for line in csv_file:
        reports.append(line)
    filename.close()
    del reports[0]
    return reports

def open_file():
    #Hnadling for when a file is opened at the beginning of the program.
    while True:
        try:
            filename = input('Enter a file ==> ')
            file = open(filename, encoding = 'utf-8')
            return file
        except FileNotFoundError:
            print('Could not open file', filename)
        except IOError:
            print('IO Error attempting to open', filename)

def create_reported_date_dict(reports_list):
    #Generates a dict containing the number of crimes reported per day.
    date_dict = {}
    for report in reports_list:
        if report[1] in date_dict:
            date_dict[report[1]] = date_dict[report[1]] + 1
        else:
            date_dict[report[1]] = 1
    return date_dict


def create_reported_month_dict(reports_list):
    #Generates a dict containing the number of crimes reported per month.
    month_dict = {}
    for report in reports_list:
        date = report[1].split('/')
        month = month_from_number(date[0])
        if month in month_dict:
            month_dict[month] = month_dict[month] + 1
        else:
            month_dict[month] = 1
    return month_dict

def create_offense_dict(reports_list):
    #Generates a dict containing the number of crimes reported per type of crime.
    offense_dict = {}
    for report in reports_list:
        if report[7] in offense_dict:
            offense_dict[report[7]] = offense_dict[report[7]] + 1
        else:
            offense_dict[report[7]] = 1
    return offense_dict

def create_offense_by_zip(reports_list):
    #Asks the user for an offense, then displays the zip code and crime counts associated with the offense.
    #TODO: Fix this mess
    offense_zips = {}
    while True:
        try:
            offense = input('Enter an offense ==> ')
            for report in reports_list:
                if offense == report[7]:
                    offense_zips[report[7]] = {report[13]: 1}
            return offense_zips
        except KeyError:
            print('That offense does not exist in the database. Please try again.')


if __name__ == '__main__':
    #Opens a user's desired file
    reports_file = read_in_file(open_file())
    #Ouputs the month with the highest number of crime occurences.
    print('Month with highest crime rate:', max(create_reported_month_dict(reports_file), key=create_reported_month_dict(reports_file).get))
    #Outputs the offense that occurred the most.
    print('Most common offense:', max(create_offense_dict(reports_file), key=create_offense_dict(reports_file).get))
    #Asks the user for an offense, then displays the zip code and crime counts associated with the offense.
    print(create_offense_by_zip(reports_file))