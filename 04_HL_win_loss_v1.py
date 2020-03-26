# HL Component 4 - Win and Loss mechanics

secret = 7
guesses_allowed = 4

guesses_left = guesses_allowed
num_won = 0

guess = ""

while guess != secret and guesses_left >= 1:

    guess = int(input("Guess: "))
    guesses_left -= 1

    if guesses_left >= 1:

        if guess < secret:
            print("Too low, try a higher number")
        elif guess > secret:
            print("Too high, try a lower number")
        else:
            if guess < secret:
                print("Too low!")
            elif guess > secret:
                print("Too High")

if guess == secret:
    if guesses_left == guesses_allowed - 1:
        print("Amazing! You got it one guess")
    else:
        print("Well Done, you got it in {} guesses".format(guesses_allowed - guesses_left))
        num_won += 1
else:
    print("Sorry, you lost")
