# Task 03 - Banking Console Application
# Kiran Academy | Python

def main():
    balance = 10000.0

    print("Welcome to Kiran Bank")
    print(f"Opening Balance: ₹{balance:.0f}")

    while True:
        print("\n1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            print(f"Current Balance: ₹{balance:.2f}")

        elif choice == "2":
            amount_text = input("Enter deposit amount: ").strip()
            try:
                amount = float(amount_text)
            except ValueError:
                print("Invalid amount. Please enter a valid number.")
                continue

            if amount <= 0:
                print("Invalid amount. Deposit amount must be greater than zero.")
            else:
                balance += amount
                print("Deposit successful.")
                print(f"Updated Balance: ₹{balance:.2f}")

        elif choice == "3":
            amount_text = input("Enter withdrawal amount: ").strip()
            try:
                amount = float(amount_text)
            except ValueError:
                print("Invalid amount. Please enter a valid number.")
                continue

            if amount <= 0:
                print("Invalid amount. Withdrawal amount must be greater than zero.")
            elif amount > balance:
                print("Transaction failed: Insufficient balance.")
                print(f"Current Balance: ₹{balance:.2f}")
            else:
                balance -= amount
                print("Withdrawal successful.")
                print(f"Updated Balance: ₹{balance:.2f}")

        elif choice == "4":
            print("Thank you for banking with us. Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
