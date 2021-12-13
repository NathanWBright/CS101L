########################################################################
##
## CS 101 Lab
## Program 13
## Nathan Bright
## nwbbdf@umsystem.edu
##
## PROBLEM: Use the turtle module to draw basic shapes.
##
## ALGORITHM: 
##      1. 
##      2. 
##      3. 
## 
## ERROR HANDLING:
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
