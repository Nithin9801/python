import random
from wordlist import word


# set of dexcription of key(0to6):value(ascii art)
hangman_art = {0:("   ",
                  "   ",
                  "   "),
               1:(" o ",
                  "   ",
                  "   "),
               2:(" o ",
                  " | ",
                  "   "),
               3:(" o ",
                  "/| ",
                  "   "),
               4:(" o ",
                  "/|\\",
                  "   "),
               5:(" o ",
                  "/|\\",
                  "/  "),
               6:(" o ",
                  "/|\\",
                  "/ \\"),}

def display_hangman(wrong_guess):
   print("*************")
   for line in hangman_art[wrong_guess]:
      print(line)
   print("*************")

def diplay_hint(hint):
   print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
   answer = random.choice(word)
   hint = ["_"]*len(answer)
   wrong_guess = 0
   guesses = set()
   is_running = True

   while is_running:
      display_hangman(wrong_guess)
      diplay_hint(hint)
      guess = input("enter a single letter : ").lower()


      if len(guess) != 1 or guess.isdigit():
         print("invalid input")
         continue

      if guess in guesses:
         print(f"{guess} is already guessed")
         continue
      
      guesses.add(guess)


      if guess in answer:
         for i in range(len(answer)):
            if answer[i] == guess:
               hint[i] = guess
      else:
         wrong_guess += 1

      if "_" not in hint:
         display_hangman(wrong_guess)
         display_answer(answer)
         print("you win!")
         is_running = False
      elif wrong_guess >= len(hangman_art) - 1:
         display_hangman(wrong_guess)
         display_answer(answer)
         print("you lose")
         is_running = False


if __name__ == "__main__":
    main()  