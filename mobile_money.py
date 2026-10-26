pin = "1234"
balance = 5000
deposit = 0
send_money = 0
withdraw = 0
attempt = 0
option = 0
entered_amount = 0
fee_cost = 0
mini_statement = []

while True:#intialization of while loop
    entered_pin = input("enter your pin: ")
    if entered_pin == pin:
        break

    attempt += 1
    print(f"attempt {attempt} is wrong")
    if attempt == 3:
        print("your account is blocked")
        raise SystemExit

while True: #mobile menu option selection
    print("\n--- Phone Banking Menu ---")
    print("0 enter pin to check balance")
    print("1. Check Account Balance")
    print("2. Deposit")
    print("3. Send Money")
    print("4. Withdraw Cash")
    print("5. Mini Statement")
    print("6. Exit")

    option = input("select options above: ")

    if option == "0":
        print(f"Your current balance is: {balance}")

    elif option == "1":
        print(f"Your current balance is: {balance}")

    elif option == "2":
        amount = float(input("Enter deposit amount: "))
        if amount <= 0:
            print("Invalid amount. Please enter a positive value.")
        else:
            balance += amount
            mini_statement.append(f"Deposited: {amount}")
            print(f"Successfully deposited {amount}. New balance: {balance}")

    elif option == "3":
        entered_amount = float(input("Enter amount to send: "))
        if 100 <= entered_amount <= 1000:
            fee_cost = 13
        elif 1001 <= entered_amount < 5000:
            fee_cost = 55
        elif entered_amount >= 5000:
            fee_cost = 100
        else:
            fee_cost = 0

        total_cost = entered_amount + fee_cost
        if entered_amount <= 0 or total_cost > balance:
            print("Iinsufficient funds. Please check your balance.")
        else:
            balance -= total_cost
            send_money = entered_amount
            mini_statement.append(f"Sent: {entered_amount}, Fee: {fee_cost}")
            print(f"Successfully sent {entered_amount}. Fee: {fee_cost}. New balance: {balance}")

    elif option == "4":
        amount = float(input("Enter withdrawal amount: "))
        withdrawal_fee = 30
        total_cost = amount + withdrawal_fee
        if amount < 50 or amount % 50 != 0 or total_cost > balance:
            print("insufficient funds. Please check your balance.")
        else:
            balance -= total_cost
            mini_statement.append(f"Withdrew: {amount}, Fee: {withdrawal_fee}")
            print(f"Successfully withdrew {amount}. Fee: {withdrawal_fee}. New balance: {balance}")

    elif option == "5":
        print("\n--- Mini Statement ---")
        if mini_statement:
            for transaction in mini_statement:
                print(transaction)
        else:
            print("No transactions yet.")

    elif option == "6":
        print("Exiting... Thank you for using Phone Banking!")
        break

    else:
        print("Invalid option. Please select between 0-6.")













            