#guess random number game
import random

# set random number between 1 dn 20
secretNumber = random.randint(1,20)
print("i am thinking of a number between 1 and 20")

#ask player to guess 6x
for guessTaken in range(1,7):
    print("take a guess")
    # guess is input only in int
    guess = int(input())

    # if guess is less than set number; return str, or over secret, return string; otherwise break loop
    if guess < secretNumber:
        print("your guess is too low")
    elif guess > secretNumber:
        print("your guess is too high")
    else: 
        break #correct guess

# if guess is correct, output number of attempts, only get 6 attempts, otherwise return secret num if not guessed
if guess == secretNumber:
    print("you guess my number in " + str(guessTaken) + " guesses")
else: 
    print("the number i was thinking of was " + str(secretNumber))