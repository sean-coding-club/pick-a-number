import random

low = 1
high = 10
pick = random.randint(low, high)

def guess_number():
    return int(input("Pick A Number: "))

print("Welcome to pick-a-number!")
guess = guess_number()

# Use these if you need to cheat :)
# print(pick)
# print(guess)

while guess != pick:
    print("Nice Try! Guess Again!")
    guess = guess_number()

print("CONGRATULATIONS! YOU GUESSED RIGHT!")



