import random

def number_generator():
    number = random.randint(0, 10)
    return number


secret_number = number_generator()

while True:
    guess = int(input("Guess the secret number from (0 to 10): "))

    if guess == secret_number:
        print(f"Congrats !\n{secret_number} was the secret number")
        break
    elif guess > secret_number:
        print(f"Too high !\nPlease retry.")
    elif guess < secret_number:
        print(f"Too low !\nPlease retry.")


