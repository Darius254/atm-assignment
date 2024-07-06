# Initialize balance
balance = 1000  

# Main ATM choices loop
while True:
    # To display the menu options
    print("\nWelcome to the ATM:")
    print("1. Check balance")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Exit")
    
    # Geting the user's choice
    choice = input("Enter your choice (1-4): ")
    
    # Process user's choice
    if choice == '1':
        # Check balance
        print(f"Your balance is Ksh. {balance}")
    elif choice == '2':
        # Deposit money
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            balance = balance + amount
            print(f"Deposited Ksh. {amount}. Your new balance is Ksh. {balance}")
        else:
            print("Invalid amount. Deposit amount must be greater than zero.")
    elif choice == '3':
        # Withdraw money
        amount = float(input("Enter amount to withdraw: "))
        if amount > 0:
            if balance >= amount:
                balance = balance - amount
                print(f"Withdrew Ksh. {amount}. Your new balance is Ksh. {balance}")
            else:
                print("Insufficient funds!")
        else:
            print("Invalid amount. Withdraw amount must be greater than zero.")
    elif choice == '4':
        # Exit the program
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")
