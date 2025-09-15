balance = 5000

pin = "1234"

sucess = False

for attempt in range(3):
    entered_pin = input("Enter your PIN: ")
    if entered_pin == pin:
        sucess = True
        print("Accesss granted.") 
        break
    else:
     print("Incorrect PIN. Try again.")

if not sucess:
    print("Access denied. Card blocked.")

else:
    while True:
        print("\n------ ATM Menu -----")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            print("Your balance is: $", balance)

        elif choice == "2":
            amount = int(input("Enter amount to withdraw: $"))
            if amount <= balance:
                balance -= amount
                print(f"Withdraw successful. Remaining balance: {balance} PKR")
            else:
                print("Insufficient Balance.") 

        elif choice == "3":
            deposit = int(input("Enter amount to deposit: $"))
            balance += deposit
            print("Deposit successful. New Balance is :{balance}Pkr")
        
        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
            break