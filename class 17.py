print("\n--- Welcome To Simple ATM ---")

balance = 10000

pin = int(input("Enter Your Pin: "))

if pin == 1234:
    print("\nLogin Successful")
    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")
else:
    print("Invalid Pin")
    exit()

choose = int(input("Choose Your Option: "))

if choose == 1:
    print("Your Balance is: ", balance)

elif choose == 2:
    withdraw = int(input("Enter Amount to Withdraw: "))
    if withdraw > 0:
        if withdraw <= balance:
            balance -= withdraw
            print("Please Collect Your Cash")
            print("Your New Balance is: ", balance)
        else:
            print("Insufficient Balance")
    else:
        print("Invalid Amount")

elif choose == 3:
    deposit = int(input("Enter Amount to Deposit: "))
    if deposit > 0:
        balance += deposit
        print("Deposit Successful")
        print("Your New Balance is: ", balance)
    else:
        print("Invalid Amount")

else:
    print("Invalid Choice")
