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


game_start = input("Would you like to play Rock, Paper, Scissors? Type \"yes\" or \"no\": ")
if game_start.lower() == "yes":

    while game_start.lower() == "yes":

        RPS = [rock, paper, scissors]
        RC_RPS = random.choice(RPS)

        choice = input("Type 0 for rock, 1 for paper, 2 for scissors, or type \"stop\" to quit: ")

        if choice.lower() == "stop":
            print("Thanks for playing!")
            break

        if choice == "0":
            print(rock)
            print("Computer chose:")
            print(RC_RPS)
            if RC_RPS == rock:
                print("Tie game!")
            elif RC_RPS == paper:
                print("You lose!")
            else:
                print("You win!")

        elif choice == "1":
            print(paper)
            print("Computer chose:")
            print(RC_RPS)
            if RC_RPS == rock:
                print("You win!")
            elif RC_RPS == paper:
                print("Tie game!")
            else:
                print("You lose!")

        elif choice == "2":
            print(scissors)
            print("Computer chose:")
            print(RC_RPS)
            if RC_RPS == rock:
                print("You lose!")
            elif RC_RPS == paper:
                print("You win!")
            else:
                print("Tie game!")
        else:
            print("Please choice a valid option.")

else:
    print("Goodbye.")
