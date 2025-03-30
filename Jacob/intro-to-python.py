# age = input("Quel est ton âge?\n")

# if int(age) >= 18:
#     print("Tu es un adulte.")
# else:
#     print("Tu n'es pas un adulte.")

import random

number = random.randint(0, 100)

while True:
    guess = int(input("Guess a number between 0 and 100. \n >>> "))
    if guess == number:
        print("Congrats, you got the number right!")
        break
    elif guess < number:
        print("Your guess was too small.")
    elif guess > number:
        print("Your guess was too big.")