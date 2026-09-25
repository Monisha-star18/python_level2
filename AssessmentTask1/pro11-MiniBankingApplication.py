accounts = {}

is_running = True

while is_running:
    print("\n========== Mini Banking Application ==========")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Transaction History")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            account_number = input("Enter account number: ")

            if account_number in accounts:
                print("Account already exists.")
            else:
                name = input("Enter account holder name: ")
                balance = 0

                accounts[account_number] = {
                    "name": name,
                    "balance": balance,
                    "transactions": []
                }

                accounts[account_number]["transactions"].append(
                    "Account created"
                )

                print("Account created successfully.")

        case 2:
            account_number = input("Enter account number: ")

            if account_number in accounts:
                amount = float(input("Enter deposit amount: "))

                if amount > 0:
                    accounts[account_number]["balance"] += amount

                    accounts[account_number]["transactions"].append(
                        f"Deposited ₹{amount}"
                    )

                    print("Amount deposited successfully.")
                else:
                    print("Amount must be greater than zero.")
            else:
                print("Account not found.")

        case 3:
            account_number = input("Enter account number: ")

            if account_number in accounts:
                amount = float(input("Enter withdrawal amount: "))

                if amount <= 0:
                    print("Amount must be greater than zero.")
                elif amount > accounts[account_number]["balance"]:
                    print("Insufficient balance.")
                else:
                    accounts[account_number]["balance"] -= amount

                    accounts[account_number]["transactions"].append(
                        f"Withdrawn ₹{amount}"
                    )

                    print("Amount withdrawn successfully.")
            else:
                print("Account not found.")

        case 4:
            account_number = input("Enter account number: ")

            if account_number in accounts:
                balance = accounts[account_number]["balance"]
                print(f"Current balance: ₹{balance}")
            else:
                print("Account not found.")

        case 5:
            account_number = input("Enter account number: ")

            if account_number in accounts:
                print("\n---------- Transaction History ----------")

                transactions = accounts[account_number]["transactions"]

                for transaction in transactions:
                    print(transaction)
            else:
                print("Account not found.")

        case 6:
            print("Thank you for using the banking application.")
            is_running = False
            break

        case _:
            print("Invalid choice.")