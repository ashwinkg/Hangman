import random
import hangman_words
from hangman_art import logo, stages
  
print(logo)
word_list =hangman_words.word_list
chosen_word =random.choice(word_list)
print(f"Psst, the chosen word is {chosen_word}")
lives = 6 # number of lives the player can have

word_length =len(chosen_word)
#creating a list of length chosen_word
display =["_"]*word_length
end_game = False

while not end_game:
    guess=input("Guess a letter: ").lower()
    if guess not in chosen_word:
        print(f"You guessed '{guess}' that's not in the word. You lose a life")
        lives-=1
    else:
        if guess in display:
            print(f"You've already guessed: '{guess}'")
        else:
            for letter_index in range(word_length):
                if chosen_word[letter_index]==guess:
                    display[letter_index] = guess
    
    print(f"{' '.join(display)}")
    print(stages[lives]) 
    if lives==0:
        end_game=True
        print("You lose!")
    elif "_" not in display:
        end_game=True
        print("You won!!")
          


