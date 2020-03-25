# HL Component 9 - set up score mechanics

# To do
# Set up round and win counter
# update feedback statements

secret = 7
guesses_allowed = 4
rounds = int(input("How many rounds? "))
game_stats = []

num_won = 0
rounds_played = 0

while rounds_played < rounds:
    guess = ""
    guesses_left = guesses_allowed
    already_guessed = []

    while guess != secret and guesses_left >= 1:
        guess = int(input("Guess: "))

        if guess in already_guessed:
            print("You already guessed that number! Please enter a different number")
            print("You still have {} guesses left".format(guesses_left))
            continue

        guesses_left -= 1
        already_guessed.append(guess)

        if guesses_left < 1:
            if guess != secret:
                print()
                print("Sorry You Lost")
                guesses_left -= 1
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
                num_won += 1
                if guesses_left == 1:
                    print("You had {} guess remaining".format(guesses_left))
                else:
                    print("You had {} guesses remaining".format(guesses_left))
                break

    game_stats.append(guesses_allowed - guesses_left)
    print("Won: {} \t | \t Lost: {}".format(num_won, rounds_played - num_won + 1))
    print()
    rounds_played += 1

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

print()
print("***Summary Statistics***")
print("Best: {}".format(best))
print("Worst: {}".format(worst))
print("Average: {:.2f}".format(average))


print("Thanks for playing")
