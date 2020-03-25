# HL Component 8 - set up score mechanics

# To do
# Set up round and win counter
# update feedback statements

secret = 7
guesses_allowed = 4
rounds = 3

num_won = 0
rounds_played = 0

while rounds_played < rounds:
    guess = ""
    guesses_left = guesses_allowed

    while guess != secret and guesses_left >= 1:
        guess = int(input("Guess: "))
        guesses_left -= 1

        if guesses_left < 1:
            if guess != secret:
                print()
                print("Sorry You Lost")
                break
            else:
                print()
                print("Well done! You guessed the secret number")
                print("You got it on the final guess")
                num_won += 1
                break

        elif guess == secret and guesses_left == (guesses_allowed - 1):
            print()
            print("Sugoi, you got it first try!")
            num_won += 1

        else:
            if guess < secret:
                print("Too low, try a higher number")
                print("You still have {} guesses left".format(guesses_left))

            elif guess > secret:
                print("Too high, try a lower number")
                print("You still have {} guesses left".format(guesses_left))

            else:
                print()
                print("Well done! You guessed the secret number")
                if guesses_left == 1:
                    print("You had {} guess remaining".format(guesses_left))
                else:
                    print("You had {} guesses remaining".format(guesses_left))
                break

    print("Won: {} \t | \t Lost: {}".format(num_won, rounds_played - num_won + 1))
    print()
    rounds_played += 1

print("Thanks for playing")
