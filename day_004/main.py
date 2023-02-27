import random

#! DAY 4 - Rock paper scissors game
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
choices = [rock, paper, scissors]

user_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice >= 3 or user_choice < 0:
    print("\nYou typed an invalid number. YOU LOOSE")
else:
    print(f"You chose..\n {choices[user_choice]}")
    comp_choice = random.randint(0, 2)
    print(f"Computer chose..\n {choices[comp_choice]}")

    if user_choice == 0 and comp_choice == 2:
        print("\nYOU WON !!")
    elif comp_choice == 0 and user_choice == 2:
        print("\nYOU LOOSE !!")
    elif user_choice > comp_choice:
        print("\nYOU WON !!")
    elif comp_choice > user_choice:
        print("\nYOU LOOSE !!")
    elif user_choice == comp_choice:
        print("\nIT'S A DRAW")
