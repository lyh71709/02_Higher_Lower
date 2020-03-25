# HL Component 9b - End game stats

# To do
# Set up game play list with each round's result
# Set up average, best and worst scores

secret = 7
guesses_allowed = 4
rounds = int(input("How many rounds? "))
game_stats = []

num_won = 0
rounds_played = 0

while rounds_played < rounds:
    guess = ""
    guesses_left = guesses_allowed

    while guess != secret and guesses_left >= 1:

        guess = int(input("Guess: "))
        guesses_left -= 1

        if guesses_left >= 1:

            if guess < secret