import random

high = 100
low = 0

def number_generator():
    number = random.randint(low, high)
    return number


secret_number = number_generator()

while True:
    try:
        guess = int(input(f"Guess the secret number from ({low} to {high}): "))
    except ValueError:
        guess = -1

    if guess == secret_number:
        print(f"Congrats !\n{secret_number} was the secret number")
        break
    elif (guess > secret_number) and (guess <= high):
        print(f"Too high !\nPlease retry.")
    elif (guess < secret_number ) and (guess >= low):
        print(f"Too low !\nPlease retry.")
    else:
        print("Wrong input !")


