########################################################################
##
## CS 101 Lab
## Program 13
## Nathan Bright
## nwbbdf@umsystem.edu
##
## PROBLEM: Create unittests for basic math functions.
##
## ALGORITHM: 
##      1. Add a group of numbers and test.
##      2. Average a group of numbers and test.
##      3. Find the median of a group of numbers and test.
## 
## ERROR HANDLING:
##      1. Raises ValueError if attempting to find the median of an empty list.
##      
## OTHER COMMENTS:
##      
##
########################################################################

import math
import statistics

def total(values):
    value_total = 0
    for num in values:
        value_total += num
    return value_total

def average(values):
    if len(values) == 0:
        return math.nan
    avg = total(values) / len(values)
    return avg

def median(values):
    if len(values) == 0:
        raise ValueError
    return statistics.median(values)
