name = "Sienna"
age = 19

def anniversaire():
    global age
    age = age + 1

# print(name, ":", age)
# anniversaire()
# print(name, ":", age)

def add(a, b):
    c = a + b
    return c

# print(add(1, 2))

# import random

# girl1 = "Sienna"
# girl2 = "Hannah-Mila"

# are_friends = random.randint(0, 1)
# print(are_friends)

# if are_friends == 1:
#     print(girl1, "and", girl2, "are friends!")
# else:
#     print(girl1, "and", girl2, "are not friends!")

import random

chosen_number = random.randint(1, 100)

print("What number do you think I chose?")
while True:
    guess = int(input(">>> "))

    if guess > chosen_number:
        print("Your number is too big.")
    elif guess < chosen_number:
        print("Your number is too small.")
    else:
        print("You guessed right!")
        break