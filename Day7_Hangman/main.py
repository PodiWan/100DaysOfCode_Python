import yaml
from random_word import RandomWords

r = RandomWords()

chosen_word = r.get_random_word()
guessed_letters = ""
for i in range(len(chosen_word)):
    guessed_letters += "_"

lifes = 6

while guessed_letters != chosen_word and lifes != 0:
    print(guessed_letters)
    print(f"Lifes: {lifes}")

    user_input = input("Input a letter: ")
    if len(user_input) > 1:
        lifes -= 1
    
    if user_input in chosen_word:

        guessed_letters_list = list(guessed_letters)

        for i in range(len(chosen_word)):
            if user_input == chosen_word[i]:
                guessed_letters_list[i] = user_input
        
        guessed_letters = "".join(guessed_letters_list)
    else:
        lifes -= 1

print(guessed_letters)
print(f"Lifes: {lifes}")
print(chosen_word)

if lifes == 0:
    print("Game over!")
else:
    print("Gongratulations!")