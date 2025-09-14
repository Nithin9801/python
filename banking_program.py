def show_balance(balance):
    print("***************")
    print(f"your balance is ${balance:.2f}")
    print("***************")
    
def deposit():
    amount = float(input("enter the amount to be deposited: $"))

    if amount < 0:
        print("amount should be greater than 0")
        return 0 
    else :
        return amount
    
def withdraw(balance):
    amount = float(input("enter the amount to be withdrawn: $"))
    
    if amount > balance:
        print("isufficient funds")
        return 0
    elif amount < 0:
        print("enter the amount greater than 0")
        return 0
    else:
        return amount
    

def main():

    balance = 0
    is_running = True

    while is_running:
        print("***************")
        print("Banking Program")
        print("***************")
        print("1.showbalance")
        print("2.deposit")
        print("3.withdraw")
        print("4.exit")
        print("***************")
        
        choice = input("Enter the choice from 1-4: ")
        
        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else :
            print("invalid input")
        
    print("Thank you for choosing Nithin's bank")

if __name__ == '__main__':
    main()