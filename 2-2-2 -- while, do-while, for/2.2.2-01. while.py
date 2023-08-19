import random

secret_number = random.randint(1, 100)
guess = 0
attempts = 0

print("Welcome to the Guess the Number Game!")

while guess != secret_number:
    guess = int(input("Guess a number between 1 and 100: "))
    attempts += 1

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")

print("Congratulations! You guessed the secret number", secret_number, "in", attempts, "attempts.")