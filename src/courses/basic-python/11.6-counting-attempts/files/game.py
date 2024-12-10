import random

number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Guess the number between 1 and 100: "))

    attempts += 1
    
    if guess == number:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break
    elif guess < number:
        print("Too low. Try again.")
    elif guess > number:
        print("Too high. Try again.")