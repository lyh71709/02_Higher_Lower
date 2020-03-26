# HL Component 6 - Statement generator

def hl_statement(statement, char):
    print()
    print(char*len(statement))
    print(statement)
    print(char*len(statement))
    print()

# Main Routine

too_low = hl_statement("⬆⬆⬆  Too Low, try a higher number  ⬆⬆⬆ ", "-")

print()
too_high = hl_statement("⬇⬇⬇  Too High, try a lower number  ⬇⬇⬇ ", "-")

print()
duplicate = hl_statement("(╯°□°）╯︵ ┻━┻  You already guessed that number  ", "!")

print()
win = hl_statement("(☞ﾟヮﾟ)☞  Well Done! You got it  ☜(ﾟヮﾟ☜)    ", "-")

print()
start_round = hl_statement("🔔    Round 1 of 3    🔔  ", "-")

print()
lose = hl_statement("(╬▔皿▔)╯   Sorry You Lost    ", "-")

print()
first_try = hl_statement("✨   Sugoi! You got it first try   ✨  ", "-")

print()
welcome = hl_statement("Welcome to the Higher Lower Game!", "=")
