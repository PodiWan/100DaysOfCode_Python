class Choice:
    def __init__(self, timestamp, text, outcome):
        self.timestamp = timestamp
        self.text = text
        self.outcome = outcome

class Stage:
    def __init__(self, timestamp, text, correct_choice):
        self.timestamp = timestamp
        self.text = text
        self.correct_choice = correct_choice

choices = [
    Choice(1, "left", "",),
    Choice(1, "right", "You fell into a hole."),
    Choice(2, "wait", ""),
    Choice(2, "swim", "You get attacked by an angry trout."),
    Choice(3, "blue", "You enter a room of beasts."),
    Choice(3, "yellow", ""),
    Choice(3, "red", "It's a room full of fire.")
]

step_stages = [
    Stage(1, "You're at a cross road. Where do you want to go?", choices[0]),
    Stage(2, "You've come to a lake. There is an island in the middle of the lake.", choices[2]),
    Stage(3, "You arrive at the island unharmed. There is a house with 3 doors.", choices[5])
]

game_status = True
step = 1

print("Welcome to Treasure Island")
print("Your mission is to find the treasure.")

while game_status:
    current_choices = [x for x in choices if x.timestamp == step]
    if current_choices == []:
        exit("You found the hidden treasure!")

    user_input = input(step_stages[step - 1].text + " Type " + str([x.text for x in current_choices]).strip('[]') + ": ")
    if user_input in [x.text for x in current_choices]:
        option = [x for x in current_choices if x.text == user_input][0]
        game_status = (option == step_stages[step - 1].correct_choice)
        if game_status == False:
            print(option.outcome)
    else:
        print("Invalid choice")
        game_status = False

    if game_status == False:
        exit("Game over")

    step += 1