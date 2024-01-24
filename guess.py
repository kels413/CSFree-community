"""Educational guess the secret code game in python"""
# generate random numbers for bot choice and secret code
import random
import time

secret_code = random.randint(1, 9)
bot_choice = random.randint(1, 9)
print(secret_code)

bot_message = ["oh dear, you missed the mark!❌ Let me show you how it's done.💯",
               "Nice try, human!🧔 Now, watch📺 and learn.📝",
               "Oh, almost there 😹, but not quite! Allow me to demonstrate precision. 🏹",
               "A valiant effort😡, but no luck this time😹! Time for the bot to shine.💃🏽"
               ]
user_highe
bot_message_random = random.randint(0, 3)
bot_messages = bot_message[bot_message_random]

user_input = int(input("what's your choice "))

while True:
    if user_input != secret_code:
        print(bot_messages)
        print("Bot Thinking 🤔...")
        time.sleep(1)
        print("Bot Thinking 🤔...")
        time.sleep(1)
        if bot_choice != secret_code:
            print(f"Wrong choice: {bot_choice} 🤖")
            user_input = int(input("what's your choice "))
            if user_input == secret_code:
                print("you won")
                exit(0)
        else:
            print("bot won")
            exit(0)
    else:
        print("you won")
        exit(0)
