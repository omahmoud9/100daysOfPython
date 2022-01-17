import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
choice = int(
    input(
        "What do you choose? Type 0 for rock, 1 for Paper or 2 for Scissors. \n"
    ))
if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
else:
    print(scissors)

print("Computer chose: \n")
choice1 = random.randint(0, 2)

if choice1 == 0:
    print(rock)
    if choice == 0:
        print("Tie Game")
    elif choice == 1:
        print("Paper beats Rock. You Win!")
    elif choice == 1:
        print("Rock beats Scissors. You Lose!")
elif choice1 == 1:
    print(paper)
    if choice == 0:
        print("Paper beats Rock. You Win!")
    elif choice == 1:
        print("Tie Game")
    elif choice == 1:
        print("Scissors beats Paper. You Lose!")
else:
    print(scissors)
    if choice == 0:
        print("Rock beats Scissors. You Lose!")
    elif choice == 1:
        print("Scissors beats Paper. You Win!!")
    elif choice == 1:
        print("Tie Game")
