pin = "1234"
balance = 5000
deposit = 0
send_money = 0
withdraw = 0
attempt = 0
option = 0
entered_amount = 0
fee_cost = 0

while True:
    entered_pin = input("enter your pin: ")
    if entered_pin == pin:
        check = input("check your balance? (yes or no): ").lower()
        if check == "yes":
            print("check your balance is: " + str(balance))
        break
    else:
        attempt += 1
        print(f"attempt {attempt} is wrong")
        if attempt == 3:
            print("your account is blocked")
            raise SystemExit

print("\n2. deposit money")
print("3. send money")
print("4. withdraw money")

option = input("select options above: ")

if option == "2":
    deposit = int(input("enter deposit amount: "))
    balance += deposit
    print("your new balance is: " + str(balance))

elif option == "3":
    print("selected send money")
    entered_amount = int(input("enter amount: "))

    if 100 <= entered_amount <= 1000:
        fee_cost = 13
    elif 1001 <= entered_amount < 5000:
        fee_cost = 55
    elif entered_amount >= 5000:
        fee_cost = 100
    else:
        fee_cost = 0

    send_money = entered_amount - fee_cost
    balance -= entered_amount

    print("entered_amount is: " + str(entered_amount))
    print("fee_cost is: " + str(fee_cost))
    print("send_money is: " + str(send_money))
    print("your new balance is: " + str(balance))

elif option == "4":
    print("selected withdraw money")
    withdraw = int(input("enter withdrawal amount: "))
    if withdraw >= 50 and withdraw <= balance:
        withdraw_fee = 30
        balance -= withdraw + withdraw_fee
        print("withdraw_fee is: " + str(withdraw_fee))
        print("withdraw_money: " + str(withdraw))
        print("your new balance is: " + str(balance))
    else:
        print("insufficient balance")
        print("your new balance is: " + str(balance))
else:
    print("invalid option")
            