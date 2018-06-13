from random import randint

# Create the moves and initialize points
moves = ['ROCK', 'PAPER', 'SCISSOR']
userWins = 0
pcWins = 0

while(1):
    # Pick a move for the computer
    randomChoice = randint(0, len(moves) - 1)
    computerChoice = moves[randomChoice]

    # Take an raw_input from the user and capitalize it
    userChoice = (raw_input("\nPlease type in one of the following: Rock, Paper, Scissor or Exit\n\n")).upper()

    # If user exits: break
    if (userChoice == 'EXIT'):
        break

    # Print user, computer options
    print "\nYou selected: ", userChoice
    print "Computer selected: ", computerChoice

    # If the user and computer have the same choices
    if (userChoice == computerChoice):
        print "\nNo one won this round."
        print "USER WINS:", userWins
        print "COMPUTER WINS:", pcWins

    # If the user chose ROCK
    if (userChoice == 'ROCK'):
        # If the computer chose PAPER
        if (computerChoice == 'PAPER'):
            print "\nThe computer beat you this round."
            pcWins += 1
            print "USER WINS:", userWins
            print "COMPUTER WINS:", pcWins
        # If the computer chose SCISSOR
        if (computerChoice == 'SCISSOR'):
            print "\nYou beat the computer this round."
            userWins += 1
            print "USER WINS:", userWins
            print "COMPUTER WINS:", pcWins

    # If the user chose PAPER
    if (userChoice == 'PAPER'):
        # If the computer chose SCISSOR
        if (computerChoice == 'SCISSOR'):
            print "\nThe computer beat you this round."
            pcWins += 1
            print "USER WINS:", userWins
            print "COMPUTER WINS:", pcWins
        # If the computer chose ROCK
        if (computerChoice == 'ROCK'):
            print "\nYou beat the computer this round."
            userWins += 1
            print "USER WINS:", userWins
            print "COMPUTER WINS:", pcWins

    # If the user chose SCISSOR
    if (userChoice == 'SCISSOR'):
        # If the computer chose ROCK
        if (computerChoice == 'ROCK'):
            print "\nThe computer beat you this round."
            pcWins += 1
            print "USER WINS:", userWins
            print "COMPUTER WINS:", pcWins
        # If the computer chose PAPER
        if (computerChoice == 'PAPER'):
            print "\nYou beat the computer this round."
            userWins += 1
            print "USER WINS:", userWins
            print "COMPUTER WINS:", pcWins

    if (userChoice != 'ROCK' and userChoice != 'PAPER' and userChoice != 'SCISSOR'):
        print "\nYour input wasn't one of the above options"
