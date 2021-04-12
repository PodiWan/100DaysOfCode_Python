import random

options = ["rock", "paper", "scissors"]
options_visual = [
    "\n\
---'   ____) \n\
    (_____) \n\
    (_____) \n\
    (____)  \n\
---.__(___)\n\
    ",
    " \n\
---'   ____)____ \n\
          ______) \n\
          _______) \n\
         _______) \n\
---.__________)",
    "\n\
---'   ____)____ \n\
          ______) \n\
       __________) \n\
      (____) \n\
---.__(___)"
]

formatted_string = f"What would you like to play? Select {0} for {options[0]}, {1} for {options[1]} or {2} for {options[2]}: "
user_option = int(input(formatted_string))
if user_option > 2 or user_option < 0:
    exit("Invalid input!")

computer_option = random.randrange(len(options))

print(f"\nIt's \n\n\n{options_visual[user_option]} \n\n\nvs \n\n\n{options_visual[computer_option]}\n")

if (user_option == 0 and computer_option == 2):
    print("You win!")
elif user_option < computer_option or (user_option == 2 and computer_option == 0):
    print("You lose!")
elif user_option > computer_option:
    print("You win!")
else:
    print("It's a draw!")