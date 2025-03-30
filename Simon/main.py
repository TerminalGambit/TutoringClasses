import random

garcons = ["Hugo", "Jules", "Pierre", "Sebastien"]
filles = ["Sienna", "Hannah-Mila", "Carolina", "Jennifer"]

gender = input("What are you? A boy (B) or a girl (G)?\n > ")

if gender == "B":
    print(random.choice(filles))
else:
    print(random.choice(garcons)) 