import random
from hangman_words import word_list
from hangman_art import logo, stages
from replit import clear
import requests
print(logo)
chosen_word = random.choice(word_list)
print(f'solution is {chosen_word}') #for testing

display = []
word_length = len(chosen_word)
lives = 6
for letter in range(len(chosen_word)):
    display += "_"
print(display)

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter:").lower()
    clear()
    if guess in display:
        print(f"You have already guessed the letter.")
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            print(display)
    if guess not in chosen_word:
        print("You guessed the wrong letter. You lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose!!")
    if "_" not in display:
        end_of_game = True
        print("You have Won!!")
    print(stages[lives])