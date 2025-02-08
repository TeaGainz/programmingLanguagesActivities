def main():
    yearly_rate = 0.025
    balance = 0.0

    while True:
        print("\n[d] – Deposit")
        print("[w] – Withdrawal")
        print("[x] – Exit")
        option = input("Option: ").lower()

        if option == 'x':
            break

        print(f"\nBeginning of Month Balance: {balance:.2f}")

        if option == 'd':
            amount = float(input("Enter the deposit amount: "))
            balance += amount
        elif option == 'w':
            amount = float(input("Enter the withdrawal amount: "))
            if amount > balance:
                print("Insufficient funds for withdrawal.")
                continue
            balance -= amount
        else:
            print("Invalid option. Please choose 'd', 'w', or 'x'.")
            continue

        # Apply monthly interest
        balance = balance + (yearly_rate / 12) * balance

        print(f"\nBalance after a transaction: {balance:.2f}")

    print(f"\nBeginning of Month Balance: {balance:.2f}")
    print(f"Balance after a transaction: {balance:.2f}")
    print("\nThank you for Banking with us…")

if __name__ == "__main__":
    main()