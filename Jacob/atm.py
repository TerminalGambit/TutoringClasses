import datetime

balance = 0
transactions = ["#"*19]

print("Welcome to the ATM:")
print("#"*19)

def adding_transaction(type_of_transaction, amount):
    global transactions
    result = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " — "
    result = result + f"{type_of_transaction}, \t"
    if type_of_transaction == "Retrieve":
        result = result + f"-{amount}€"
    elif type_of_transaction == "Deposit":
        result = result + f"+{amount}€"
    # result += "\n"
    transactions.append(result)

# print(adding_transaction("Retrieval", 70))
# print(adding_transaction("Deposit", 30))

while True:
    print()
    print("What do you want to do?")
    print("(A): Deposit")
    print("(B): Retrieve")
    print("(C): Check Balance")
    print("(D): Transaction History")
    print("(E): Cancel")
    answer = input("> ")
    
    if answer == "A":
        print("How much money do are you depositing?")
        amount = float(input("> "))
        balance = balance + amount
        adding_transaction("Deposit", amount)

    elif answer == "B":
        while True:
            print("You have", balance, "€, on your bank account")
            print("How much do you want to retrieve?")
            print("(1): 200€")
            print("(2): 100€")
            print("(3): 50€")
            print("(4): 20€")
            print("(5): 10€")
            print("(6): Custom amount")
            answer = input("> ")

            if answer == "1":
                if balance < 200:
                    print("Error: You don't have enough money!")
                else:
                    balance = balance - 200
                    print("Here is your money: 200€")
                    print("You now have", balance, "€ on your bank account.")
                    adding_transaction("Retrieve", 200)
                    break
            
            elif answer == "2":
                if balance < 100:
                    print("Error: You don't have enough money!")
                else:
                    balance = balance - 100
                    print("Here is your money: 100€")
                    print("You now have", balance, "€ on your bank account.")
                    adding_transaction("Retrieve", 100)
                    break
            
            elif answer == "3":
                if balance < 50:
                    print("Error: You don't have enough money!")
                else:
                    balance = balance - 50
                    print("Here is your money: 50€")
                    print("You now have", balance, "€ on your bank account.")
                    adding_transaction("Retrieve", 50)
                    break
            
            elif answer == "4":
                if balance < 20:
                    print("Error: You don't have enough money!")
                else:
                    balance = balance - 20
                    print("Here is your money: 20€")
                    print("You now have", balance, "€ on your bank account.")
                    adding_transaction("Retrieve", 20)
                    break

            elif answer == "5":
                if balance < 10:
                    print("Error: You don't have enough money!")
                else:
                    balance = balance - 10
                    print("Here is your money: 10€")
                    print("You now have", balance, "€ on your bank account.")
                    adding_transaction("Retrieve", 10)
                    break

            elif answer == "6":
                amount = float(input("> "))
                if amount > balance:
                    print("Error: You don't have enough money!")
                else:
                    balance = balance - amount
                    print("You have", balance, "€ in your bank account.")
                    adding_transaction("Retrieve", amount)
                    break

            elif answer == "C":
                break
            
            else:
                print("You didn't choose a valid option.")
                print("Please try again.")

    
    elif answer == "C":
        print("You currently have", balance, "€ in your bank account.")

    elif answer == "D":
        for line in transactions:
            print(line)

    elif answer == "E":
        break
    
    else:
        print("You didn't choose a valid option.")
        print("Please try again.")
    # print('\n'*3)

# Note pour la prochaine fois : 
# Transaction history (Liste)