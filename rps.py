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
x = ("You win")
y = ("You lose")

game_choice = [rock, paper, scissors]

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user >= 3 or user < 0:
    print("You typed an invalid number, you lose!")
else:
    print(game_choice[user])

computer = random.randint(0, 2)
print("Computer chose:")
print(game_choice[computer])

if user == 0 and computer == 1:
    print(y)
elif computer == 0 and user == 1:
    print(x)
elif user == 0 and computer == 2:
    print(x)
elif computer == 0 and user == 2:
    print(y)
elif user == 1 and computer == 0:
    print(x)
elif computer == 1 and user == 0:
    print(y)
elif user == 1 and computer == 2:
    print(y)
elif computer == 1 and user == 2:
    print(x)
elif user == 2 and computer == 0:
    print(y)
elif computer == 2 and user == 0:
    print(x)
else:
    print("It's a draw!")
        
