import random as rd 

options = ("rock","paper","scissor")
running = True

while running:

    player = None
    computer = rd.choice(options)

    while player not in options :
        player = input("enter the answer")
    
    print(f"player choice : {player}")
    print(f"computer choice : {computer}")

    if player == computer :
         print("game is tie")
    elif player == "paper" and computer == "rock" :
         print("you win")
    elif player == "rock" and computer == "scissor" :
         print("youu win")
    elif player == "scissor" and computer == "paper" :
         print("you win")
    else :
         print("you loose")
 
    play_again = input(" want to play again? (y/n)").lower()
    if not play_again == "y":
      running = False

print("---thank you for playing---")     