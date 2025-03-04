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

player_choice = int(input("what do you want to choose?Type 0 for rock Type 1 for paper Type 2 for scissors..\n"))
if player_choice == 0:
    print(rock)
elif player_choice == 1:
    print(paper)
else:
    print(scissors)

computer_choice = random.randint(0, 2)
print(f"computer choose {computer_choice}")
if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
else:
    print(scissors)
# if player_choice == 1 and computer_choice == 0:
#     print("congrats!!\nyou winn..")
# else:
#     print("\n")
# if player_choice == 0 and computer_choice == 1:
#     print("oohh!\nyou lose..")
# else:
#     print("\n")
# if player_choice == 2 and computer_choice == 0:
#     print("oohh!\nyou lose..")
# else:
#     print("\n")
# if player_choice == 0 and computer_choice == 2:
#     print("congrats!!\nyou winn..")
# else:
#     print("\n")
# if player_choice == 1 and computer_choice == 2:
#     print("congrats!!\nyou winn..")
# else:
#     print("\n")
# if player_choice == 2 and computer_choice == 1:
#     print("congrats!!\nyou winn..")
# else:
#     print("\n")
# if player_choice == computer_choice:
#     print("hurrah!!\nyou both tie the game.")
# else:
#     print("\n")
if player_choice == 2 and computer_choice == 0:
    print("oohh!!you losee..")
elif player_choice == 0 and computer_choice == 1:
    print("oohh!!you loss..")
elif player_choice > computer_choice:
    print("congrats!!you winn..")
elif player_choice < computer_choice:
    print("congrats!!you winn..")
else:
    print("the game is draww..")

print("THANKS FOR PLAYING THIS GAME")

print("it,s the game of nandani mangal")



