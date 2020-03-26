# Higher Lower Game

# To do
# Add in each and every component to make one final, completed game
# Usability Test the code

import random
import math

# Number Checking function
def intcheck(question, low = None, high = None):

        # Set up error messages
    if low is not None and high is not None:
        error = "Please enter an integer between {} and {} (Inclusive)".format(low, high)
    elif low is not None and high is None:
        error = "Please enter an integer that is more than or equal to {}".format(low)
    elif low is None and high is not None:
        error = "Please enter an integer that is less than or equal to {}".format(high)
    else:
        error = "Please enter an integer"

    while True:

        try:
            response = int(input(question))

            # Checks response is not too low
            if low is not None and response < low:
                print(error)
                print()
                continue

            if high is not None and response > high:
                print(error)
                print()
                continue

            return response

        except ValueError:
            print(error)
            print()
            continue

def hl_statement(statement, char):
    print()
    print(char*len(statement))
    print(statement)
    print(char*len(statement))
    print()

welcome = hl_statement(" Welcome to the Higher Lower Game! ", "=")
print("The rules of this game are simple")
print()
print("The computer will select a random number between the boundaries of your choosing after this, \n"
      "and your goal is to attempt to guess the random number the computer chooses. The game will tell\n"
      " you if your guess was lower or higher than the selected number. You will lose when you take too \n"
      "many guesses and the game will also tell you how many guesses you have until you lose so guess wisely.")
print()
print("Good Luck and have fun! o(*^▽^*)┛")
print()

# Begin whole game loop here
keep_going = ""
while keep_going == "":

    # Get user input for boundaries
    low = intcheck("What is your low boundary? ")
    high = intcheck("What is your high boundary? ", low + 1)

    # Ask user for how many rounds
    rounds = intcheck("How many rounds? ", 1)
    game_stats = []

    # Maximum guesses calculator
    print()
    range = high - low + 1
    max_raw = math.log2(range)
    max_upped = math.ceil(max_raw)
    guesses_allowed = max_upped + 1
    print("You will have {} guesses each round to start with".format(guesses_allowed))

    num_won = 0
    rounds_played = 0

    # Begin game
    while rounds_played < rounds:

        # Get randomly generated secret number
        secret = random.randint(low, high)

        guess = ""
        guesses_left = guesses_allowed
        already_guessed = []

        # User message letting them know what round it is
        start_round = hl_statement("🔔    Round {} of {}    🔔  ".format(rounds_played + 1, rounds), "-")

        # Comparisons
        while guess != secret and guesses_left >= 1:
            guess = intcheck("What is your guess?  ", low, high)

            if guess in already_guessed:
                duplicate = hl_statement("(╯°□°）╯︵ ┻━┻  You already guessed that number  ", "!")
                print("Please enter a different number, you still have {} guesses left".format(guesses_left))
                continue

            already_guessed.append(guess)
            guesses_left -= 1

            # Lose/Final guess Situation
            if guesses_left < 1:
                if guess != secret:
                    lose = hl_statement("(╬▔皿▔)╯   Sorry You Lost    ", "-")
                    print("The secret number was {}".format(secret))
                    guesses_left -= 1
                    break
                else:
                    win = hl_statement("(☞ﾟヮﾟ)☞  Well Done! You guessed the secret number  ☜(ﾟヮﾟ☜)    ", "-")
                    print("You got it on the final guess")
                    num_won += 1
                    break

            # First Try situation
            elif guess == secret and guesses_left == (guesses_allowed - 1):
                first_try = hl_statement("✨   Sugoi! You got it first try   ✨  ", "-")
                num_won += 1

            # Higher Lower guess comparison
            else:
                if guess < secret:
                    too_low = hl_statement("⬆⬆⬆  Too Low, try a higher number  ⬆⬆⬆ ", "-")
                    print("You still have {} guesses left".format(guesses_left))

                elif guess > secret:
                    too_high = hl_statement("⬇⬇⬇  Too High, try a lower number  ⬇⬇⬇ ", "-")
                    print("You still have {} guesses left".format(guesses_left))

                # Win situation
                else:
                    win = hl_statement("(☞ﾟヮﾟ)☞  Well Done! You guessed the secret number  ☜(ﾟヮﾟ☜)    ", "-")
                    num_won += 1
                    if guesses_left == 1:
                        print("You had {} guess remaining".format(guesses_left))
                    else:
                        print("You had {} guesses remaining".format(guesses_left))
                    break

        # Add to game stats list and display how many the user has won and lost so far
        game_stats.append(guesses_allowed - guesses_left)
        print("Won: {} \t | \t Lost: {}".format(num_won, rounds_played - num_won + 1))
        print()
        rounds_played += 1

    # Display total scores
    print("*** Game Scores ***")
    list_count = 1
    for item in game_stats:

        # Indicates if game has been won or lost
        if item <= guesses_allowed:
            status = "won"
        else:
            status = "lost"

        print("Round {}: {} ({})".format(list_count, item, status))
        list_count += 1

    # Calculate statistics
    game_stats.sort()
    best = game_stats[0]
    worst = game_stats[-1]
    average = sum(game_stats)/len(game_stats)

    # Display statistics
    print()
    print("***Summary Statistics***")
    print("Best: {}".format(best))
    print("Worst: {}".format(worst))
    print("Average: {:.2f}".format(average))

    # Farewell and ask user whether they want to loop the game or end it
    print()
    print("Thanks for playing ╰(*°▽°*)╯")
    keep_going = input("Press <enter> to play again or any key to quit: ")
    print()
