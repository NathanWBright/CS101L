########################################################################
##
## CS 101 Lab
## Program 11
## Nathan Bright
## nwbbdf@umsystem.edu
##
## PROBLEM: We need to create a class that can track and display time.
##
## ALGORITHM: 
##      1. Initialize clock variables.
##      2. Ask the user for the current time in hours, minutes, and seconds.
##      3. Begin counting time from this point forward.
##      4. Display the current time.
## 
## ERROR HANDLING:
##      
## OTHER COMMENTS:
##      
##
########################################################################

import time
seconds = 0

class Clock:
    #Initial variables.
    def __init__(self, hour = 0, minute = 0, second = 0, clocktype = 1):
        Clock.hour = hour
        Clock.minute = minute
        Clock.second = second
        Clock.clocktype = clocktype

    def __str__(self):
        #Display the current time appropriately, has checks for gimmicks of the AM/PM format such as 11:59:59 turning to 12:00:00 and not 00:00:00.
        if Clock.clocktype == 0:
            return '{:02}:{:02}:{:02}'.format(Clock.hour, Clock.minute, Clock.second)
        else:
            if Clock.hour == 0:
                return '12:{:02}:{:02} am'.format(Clock.minute, Clock.second)
            elif Clock.hour < 12:
                return '{:02}:{:02}:{:02} am'.format(Clock.hour, Clock.minute, Clock.second)
            elif Clock.hour == 12:
                return '12:{:02}:{:02} pm'.format(Clock.hour, Clock.minute, Clock.second)
            else:
                return '{:02}:{:02}:{:02} pm'.format(Clock.hour - 12, Clock.minute, Clock.second)

    def tick(self):
        #Processes every second, and increments the time with various checks.
        if Clock.second < 59:
            Clock.second += 1
        else:
            Clock.second = 0
            if Clock.minute < 59:
                Clock.minute += 1
            else:
                Clock.minute = 0
                if Clock.hour < 23:
                    Clock.hour += 1
                else:
                    Clock.hour = 0

if __name__ in '__main__':
    current_hour = int(input('What is the current hour? ==> '))
    current_minute = int(input('What is the current minute? ==> '))
    current_second = int(input('What is the current second? ==> '))
    #Initial time.
    set_clock = Clock(current_hour, current_minute, current_second)
    while True:
        #The loop to increment and display time.
        print(set_clock)
        Clock.tick(set_clock)
        time.sleep(1)
