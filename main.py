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


games = [rock, paper, scissors]

selected_type = int(input("What do you choose? Type 0 Rock, type 1 for Paper or 2 for Scissor.\n"))
while selected_type >= 3:
  print("Please choose the selected number!")
  selected_type = int(input("What do you choose? Type 0 Rock, type 1 for Paper or 2 for Scissor.\n"))
print(games[selected_type])

  
random_choice = random.randint(0,2)
random_picture = games[random_choice]
print(f"Computer choose:\n{random_picture}")

if selected_type > 2:
  print("try again")
elif selected_type == 0 and random_choice == 1:
  print("You lose")
elif selected_type == 2 and random_choice == 0:
  print("You lose")
elif selected_type == 1 and random_choice == 2:
  print("You lose")
elif selected_type == 0 and random_choice == 2:
  print("You win")
elif selected_type == 1 and random_choice == 0:
  print("You win")
elif selected_type == 2 and random_choice == 1:
  print("You win")
else:
  print("It's draw")
  

        





