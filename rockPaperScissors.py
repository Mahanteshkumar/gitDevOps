import random
rock = "*"
paper = "||"
scissor = "x"
game_images= [rock, paper, scissor]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice >= 3 or user_choice < 0:
    print("You typed an envalid number, you lose!")
else:
    print(game_images[user_choice])
    computer_choice = random.randint(0, 2)
    print(game_images[computer_choice])
    if user_choice == 0 and computer_choice == 2:
        print("you win!")
    elif computer_choice == 0 and user_choice == 2:
        print("you lose")
    elif computer_choice > user_choice:
        print("you lose")
    elif computer_choice < user_choice:
        print("you win!")
    elif computer_choice == user_choice:
        print("It's a draw")
