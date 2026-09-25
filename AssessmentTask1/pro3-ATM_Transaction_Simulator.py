account = {
    "accountNumber": 101011,
    "holderName": "Monisha",
    "holderAge": 20,
    "pin": "1234",
    "balance": 0,
    "transactions": ["Account created"]
}

is_running = True

while is_running:

    print("\n========== ATM Transaction Simulator ==========")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Change PIN")
    print("5. Transaction History")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            print("\n---------- Check Balance ----------")

            entered_pin = input("Enter your PIN: ")

            if entered_pin == account["pin"]:
                print(f"Account holder: {account['holderName']}")
                print(f"Current balance: ₹{account['balance']}")
            else:
                print("Incorrect PIN.")

        case 2:
            print("\n---------- Deposit ----------")

            entered_pin = input("Enter your PIN: ")

            if entered_pin == account["pin"]:
                amount = float(input("Enter deposit amount: "))

                if amount > 0:
                    account["balance"] += amount
                    account["transactions"].append(
                        f"Deposited ₹{amount}"
                    )

                    print("Amount deposited successfully.")
                    print(f"New balance: ₹{account['balance']}")
                else:
                    print("Amount must be greater than zero.")
            else:
                print("Incorrect PIN.")

        case 3:
            print("\n---------- Withdraw ----------")

            entered_pin = input("Enter your PIN: ")

            if entered_pin == account["pin"]:
                amount