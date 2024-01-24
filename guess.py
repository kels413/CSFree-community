"""A Guess the secret code game"""

print("A guess game ")

import random
import time
while  True:
    secret_code = random.randint(1, 9)
    bot_choice = random.randint(1, 9)

    print(secret_code)
    print(bot_choice)
    user_input = input("Your Choice: ")

    try:
        user_input = int(user_input)
    except Exception:
        user_input = input("Your Choice: ")

    while True:
        if user_input == secret_code:
            print("user won")
            if bot_choice in range(1, 5):
                print("im not afraid man, keep it rolling")
        elif bot_choice == secret_code:
            print("you won")
        else:
            print("you lost")



