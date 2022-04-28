# 1. Change number range from 1 to 1million
# 2. game should ask to guess the number
# 3. game should tell you if you are too high or too low
# 4. game should tell you if you guessed the number
# 5. game should tell you how many guesses it took you

from random import randint

while True:
    print("\nWelcome to 'Guess The Number'!")
    print("\nI'm thinking of a number between 1 and 1,000.\n")
    print("You have five tries to guess what number I'm thinking of.")
    print("Type 'exit' to end the game.\n")

    # set the initial values
    the_number = randint(1, 1000)
    guesses = 0
    low = 1
    high = 1000

    # loop five times, with each guess
    for guesses in range(1, 6):
        guess = int(input("Take a guess: "))

        # if user types exit, break out of loop
        if guess == "exit":
            break

        # if guess is too low, print too low message and update low
        if guess < the_number:
            print("Your guess is too low.")
            low = guess
            print("You have {} guesses left.\n".format(5 - guesses))

        # if guess is too high, print too high message and update high
        if guess > the_number:
            print("Your guess is too high.")
            high = guess
            print("You have {} guesses left.\n".format(5 - guesses))

        # if guess is correct, print correct message and break out of loop
        if guess == the_number:
            print("Your guess is correct.\n")
            break

    # if user types exit, break out of loop
    if guess == "exit":
        break

    # if guess is correct, break out of loop
    if guess == the_number:
        break

    # if guess is incorrect, print incorrect message
    print("Sorry, you're out of guesses. The number was {}.".format(the_number))
