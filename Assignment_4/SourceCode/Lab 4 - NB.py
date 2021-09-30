########################################################################
##
## CS 101 Lab
## Program 4
## Nathan Bright
## nwbbdf@umsystem.edu
##
## PROBLEM : Simulating a slot machine.
##
## ALGORITHM : 
##      1. Ask the player for a starting value of chips.
##      2. Ask the player how many chips they'd like to wager.
##      3. Randomly spin 3 "wheels" and check if they match. If they do the player earns chips, otherwise they lose chips.
##      4. Repeat 1-3 until the player runs out of chips.
##      5. Tell the player their stats, and then ask if they'd like to play again.
## 
## ERROR HANDLING:
##      Informs the player if they enter an invalid value when asked to play again, and asks again.
##      Informs the player if they enter an invalid integer when asking for wager or starting chip amount, and asks for those values again.
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

import random


def play_again() -> bool:
    ''' Asks the user if they want to play again, returns False if N or NO, and True if Y or YES.  Keeps asking until they respond yes '''
    while True:
        playagain = input('Would you like to play again? Y/YES/N/NO ==> ')
        if playagain == 'Y' or playagain == 'YES':
            return True
        elif playagain == 'N' or playagain == 'NO':
            return False
        else:
            print('Please enter either Y, YES, N, or NO, to continue.')
            continue
     
def get_wager(bank : int) -> int:
    ''' Asks the user for a wager chip amount.  Continues to ask if they result is <= 0 or greater than the amount they have '''
    while True:
        chip = int(input("Please enter the number of chips you'd like to wager ==> "))
        if chip <= 0 or chip > bank:
            print('Your wager must not be more than the number of chips you have and must be more than 0.')
            continue
        else:
            return chip        

def get_slot_results() -> tuple:
    ''' Returns the result of the slot pull '''
    slot1 = random.randint(0, 10)
    slot2 = random.randint(0, 10)
    slot3 = random.randint(0, 10)
    return slot1, slot2, slot3

def get_matches(reela, reelb, reelc) -> int:
    ''' Returns 3 for all 3 match, 2 for 2 alike, and 0 for none alike. '''
    if reela == reelb and reela == reelc:
        return 3
    elif reela == reelb or reela == reelc or reelb == reelc:
        return 2
    else:
        return 0

def get_bank() -> int:
    ''' Returns how many chips the user wants to play with.  Loops until a value greater than 0 and less than 101 '''
    while True:
        desiredchips = int(input('How many chips would you like to play with? Please enter a value between 1 and 100. ==> '))
        if desiredchips < 1 or desiredchips > 100:
            print('You must enter a value between 1 and 100.')
            continue
        else:
            return desiredchips

def get_payout(wager, matches):
    ''' Returns how much the payout is.. 10 times the wager if 3 matched, 3 times the wager if 2 match, and negative wager if 0 match '''
    if matches == 3:
        return wager * 10
    elif matches == 2:
        return wager * 3
    else:
        return wager * -1     


if __name__ == "__main__":

    print('==== Welcome to Pierson Wager ====\n')
    playing = True
    while playing:

        bank = get_bank()
        starterbank = bank
        bankmax = bank
        spins = 0

        while bank >= 1:  # Replace with condition for if they still have money.
            
            wager = get_wager(bank)

            reel1, reel2, reel3 = get_slot_results()

            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout
            if bankmax < bank:
                bankmax = bank
            spins += 1

            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()
           
        print("You lost all", starterbank, "in", spins, "spins")
        print("The most chips you had was", bankmax)
        playing = play_again()