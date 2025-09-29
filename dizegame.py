import random as rd


dice_art ={1:("┌─────────┐",
              "│         │",
              "│    ●    │",
              "│         │",
              "└─────────┘"),
           2:("┌─────────┐",
              "│  ●      │",
              "│         │",
              "│       ● │",
              "└─────────┘"),
           3:("┌─────────┐",
              "│  ●      │",
              "│    ●    │",
              "│      ●  │",
              "└─────────┘"),
           4:("┌─────────┐",
              "│  ●   ●  │",
              "│         │",
              "│  ●   ●  │",
              "└─────────┘"),
           5:("┌─────────┐",
              "│  ●   ●  │",
              "│    ●    │",
              "│  ●   ●  │",
              "└─────────┘"),
           6:("┌─────────┐",
              "│  ●   ●  │",
              "│  ●   ●  │",
              "│  ●   ●  │",
              "└─────────┘"),
              }

dice = []
total = 0 

num_of_dice = int(input("enter the number of dice to be rolled : "))
for die in range(num_of_dice) :
 dice.append(rd.randint(1,6))
print(dice)

for line in range(5):
 for die in dice:
  print(dice_art.get(die)[line],end="")
 print()


for x in dice:
 total += x
print(total)