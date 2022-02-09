import random


def input_secret_num():
    try:
        while True:
            user_input = int(input("Enter a secret num (between 0 and 20): "))
            if user_input > 20 or user_input < 0:
                print("Out of range !")
            else:
                return user_input
    except ValueError as e:
        print(e)


user_num = input_secret_num()
low = 0
high = 20

while True:
    computer_num = random.randint(low, high)

    if computer_num == int(user_num):
        print(f"Congrats computer, {computer_num} was the right number")
        break
    else:
         user_input = input(f"is {computer_num} too high(h) or too low(l) ?")
         if user_input == "h" or user_input == "H":
            high = computer_num - 1
         elif user_input == "l" or user_input == "L":
             low = computer_num + 1
         else:
             print("Wrong input !")







