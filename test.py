from random import randrange

chances = 1
number = randrange(100)

print("Welcome to our number guessing game.")
while chances <= 10:
    guess = int(input("guess my number(hint: its between 0 and 100) - "))
    if guess == number:
        print("CONGRATULATIONS! ITS THE RIGHT NUMBER!!")
        break
    else:
        if guess > number:
            print("Your guess was too high, try guessing something lower than",guess)
            chances += 1
        else:
            print("Your guess was too low, try guessing something higher than",guess)
            chances += 1

if guess != number:
    print("You have lost the game... the number was",number)


# code to play again

'''playAgain = str(input("Wanna play again? (y/n) - "))
if playAgain == "y":
    chances = 1
else:
    print("Okay, nice to play with you! goodbye.")'''

