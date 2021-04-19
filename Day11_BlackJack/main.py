import random

def random_card():
    return random.randrange(2, 12)

def too_many_points(s):
    return s > 21

def end_game(user_sum, computer_sum):
    if too_many_points(user_sum) == True:
        return False
    elif too_many_points(computer_sum) == True:
        return True
    elif user_sum > computer_sum:
        return True
    else:
        return False

def who_won(user_sum, computer_sum):
    who_won_var = end_game(user_sum, computer_sum)
    if who_won_var == False:
        exit("The dealer wins!")
    else:
        exit("The user wins!")

user_cards = []
computer_cards = []

user_cards.append(random_card())

while True:
    user_cards.append(random_card())
    computer_cards.append(random_card())

    user_sum = sum(user_cards)
    computer_sum = sum(computer_cards)

    print(user_cards)
    print(computer_cards)

    if too_many_points(user_sum) == True:
        user_cards = [1 if x == 12 else x for x in user_cards]
        if too_many_points(sum(user_cards)) == True:
            exit("Game over!\nThe dealer wins!")
    elif too_many_points(computer_sum) == True:
        computer_cards = [1 if x == 12 else x for x in computer_cards]
        if too_many_points(sum(computer_cards)) == True:
            exit("Game over!\nThe user wins!")
    
    user_option = input("Do you want to continue? Press 'y' to continue or 'n' otherwise: ")
    if user_option == 'n':
        who_won(user_sum, computer_sum)