# Hangman Game Project
# This is a simple implementation of the Hangman game where the user guesses letters to find a
import random
import hangman_words
import hangman_art

def check_game_over(display, lives):
    if lives == 0:
        return True, "Lose"
    elif "_" not in display:
        return True, "Win"
    else:
        return False, ""

word_list = hangman_words.word_list
stages = hangman_art.stages

chosen_word = random.choice(word_list)
print(hangman_art.logo)

lives = 6
placeholder = "_" * len(chosen_word)
guessed_letters = []
game_over = False
status = ""
print(f"\n\n Your word is : {placeholder}")
while not game_over:
    guess = input("Guess a letter: ").lower()
    if guess in guessed_letters:
        print(f"You already guess this letter try again.\n{stages[lives]}\n Your guesses until now : {", ".join(guessed_letters)}")
        continue
    guessed_letters.append(guess)
    if guess in chosen_word:
        display = ""
        for letter in range(len(chosen_word)):
            if chosen_word[letter] == guess:
                display += guess
            else:
                display += placeholder[letter]
        placeholder = display
        print(f"Good guess! Remaining lives are : {lives}\n{placeholder}")
    else:
        lives -= 1
        print(f"This letter {guess} is not in the word. You have {lives} remaining live(s)\n Your guesses until now : {", ".join(guessed_letters)}")
        print(stages[lives])
        print(placeholder)

    game_over, status = check_game_over(placeholder,lives)


if game_over == True and status == "Win":
    
    print(hangman_art.win)
elif game_over == True and status == "Lose":
    
    print(hangman_art.lose)
    print(f"Correct word was {chosen_word}!")
