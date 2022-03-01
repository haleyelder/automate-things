import random, sys

print("ROCK, PAPER, SCISSORS")

#vars to keep track of w,l,t
wins = 0
losses = 0
ties = 0


while True: # main game loop
    print( str(wins) + " Wins, " + str(losses) + " Losses, " + str(ties) + " Ties")
    while True: # player input loop
        print('enter your move (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input()
        # if input is q to quit
        if playerMove == "q":
            sys.exit() # quit program
        if playerMove == "r" or playerMove == "p" or playerMove == "s":
            break # break loop until letter is picked, then loop player input
        print("type one of r, p, s, or q")

    # display what the player choses 
    if playerMove == 'r':
        print("ROCK versus...")
    elif playerMove == 'p':
        print("PAPER versus...")
    elif playerMove == 's':
        print("SCISSORS versus...")
    
    # display computer choice
    randomNum = random.randint(1,3)
    if randomNum == 1:
        computerMove = 'r'
        print("ROCK")
    elif randomNum == 2: 
        computerMove = 'p'
        print("PAPER")
    elif randomNum == 3:
        computerMove = 's'
        print("SCISSORS")

    # display and record w/l/t
    if playerMove == computerMove:
        print("it's a tie")
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print("you win!")
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print("you win!")
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print("you win!")
        wins = wins + 1
    elif playerMove == "r" and computerMove == 'p':
        print('you lose!')
        losses = losses +1 
    elif playerMove == "p" and computerMove == 's':
        print("you lose!")
        losses = losses + 1
    elif playerMove == "s" and computerMove == "r":
        print("you lose!")
        losses = losses + 1