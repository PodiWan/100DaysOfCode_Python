import os

def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

print("Welcome to the secret auction program.")

running = True
highest_bidder = ("", 0)

while running == True:
    user_name = input("What is your name?: ")
    
    user_bid = 0
    while user_bid <= 0:
        user_bid = int(input("What is your bid?: $"))

    should_continue = ""
    while should_continue != 'yes' and should_continue != 'no':
        should_continue = input("Are there any other bidders? Types \'yes\' or \'no\': ")
    
    if should_continue == 'no':
        running = False
    
    if user_bid > highest_bidder[1]:
        highest_bidder = (user_name, user_bid)
    clear_screen()

print(f"The winner is {highest_bidder[0]} with a bid of ${highest_bidder[1]}.")    