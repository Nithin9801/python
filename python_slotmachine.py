# python slot machine program
import random

def spin_row():
    symbols = ['🍋','🍉','🍒','⭐','🔔']

    results = [random.choice(symbols) for _ in range(3)]
    return results

def print_row(row):
    print("**************")
    print(" | ".join(row))
    print("**************")

def payout(row,bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍋':
            return bet*2
        elif row[0] == '🍉':
            return bet*3
        elif row[0] == '🍒':
            return bet*4
        elif row[0] == '⭐':
            return bet*10
        elif row[0] == '🔔':
            return bet*20
    return 0

def main():
    balance = 100

    print("***********************")
    print("Welcome to python slots")
    print("symbols:🍋 🍉 🍒 ⭐ 🔔")
    print("***********************")

    while balance > 0:
        print(f"Current balance ${balance}")

        bet = input("enter the amount you want to bet $")

        if not bet.isdigit():
            print("you cannot enter a alphabet")
            continue

        bet = int(bet)

        if bet > balance :
            print("insufficient funds")
            continue
            
        if bet <= 0:
            print("enter the amount greater than 0")
            continue

        balance -= bet
        
        row = spin_row()
        print("spinning.....\n")
        print_row(row)

        pay = payout(row,bet)
        if pay > 0:
            print(f"you got ${pay}")
        else:
            print("sorry you lose this game")

        balance += pay
        
        play_again = input("do you wnat to play again (y or n): ").upper()
        
        if not play_again == "Y":
            break
    print("Thanks for playing")
    print("*************************************")
    print(f"game over! your balance is {balance}")
    print("*************************************")

    
if __name__ == '__main__':
    main()