import random
from os import system
from art import stages

#! DAY 7 - Hangman Game
word_list = ['designer', 'available', 'specimen', 'bench', 'appetite',
             'misery', 'pneumonia', 'participate', 'pumpkin', 'package']
choosen_word = random.choice(word_list)
end_of_game = False
lives = 6

print("\nWELCOME TO HANGMAN GAME\n")

display = []
for i in range(0, len(choosen_word)):
    display.append("_")
print(f"{' '.join(display)}")

while not end_of_game:
    user_guess = input("Enter your guessed alphabet: ").lower()
    system('clear')
    if user_guess in display:
        print("You've already guessed that alphabet")
    for position in range(len(choosen_word)):
        letter = choosen_word[position]
        if letter == user_guess:
            display[position] = letter
    if user_guess not in choosen_word:
        print(
            f"OH-UH '{user_guess}' is NOT a correct guess. You loose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("YOU LOOSE")
    print(f"{' '.join(display)}")
    if '_' not in display:
        end_of_game = True
        print("YOU WIN !!!")
    print(stages[lives])
