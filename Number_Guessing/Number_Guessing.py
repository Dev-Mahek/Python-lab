import random

secret_number = random.randint(1, 10)
attempts = 0

print("🎯 Welcome to Guess the Number!")
print("I'm thinking of a number between 1 and 10")
print("Can you guess it?\n")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("📉 Too low! Try again.\n")
    elif guess > secret_number:
        print("📈 Too high! Try again.\n")
    else:
        print(f"🎉 Congratulations! You got it right in {attempts} tries!")
        break
