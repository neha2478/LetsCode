import random

#TODO-1 :- Update the word list to use the 'word_list' from hangman_words.py
from hangman_words import word_list # another way of importing list from python file
from hangman_art import stages, logo 

lives = 6 

#TODO-3 : - Import the logo from hangman_art.py and print it at the start of the game.
print(logo)

chosen_word = random.choice(word_list)  
print(chosen_word) 

placeholder = "" 
word_length = len(chosen_word) 

for index in range(word_length): 
    placeholder += "_"
print(f"Word to guess: {placeholder}")

game_over = False
correct_letters = []

while not game_over:

    # TODO-6 :- Update the code below to tell the user how many lives they have left.
    print(f"*************************{lives}/6 LIVES LEFT************************************")
    guess = input("Guess a Letter: ").lower()

    # Todo - 4 :- If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
     
    print("Word to guess: " + display) 

    #--------------------------------TODO-5 :- ----------------------------------------------------
    #TODO-5 :- If the letter is not in the chosen_word, print out the letter and let them know it in the word. 
    # e.g. You guessed d, that's not in the word. You lose a life.  
    
    if guess not in chosen_word:
        lives -= 1 
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
         
        if lives == 0: 
            game_over = True 
            
            # TODO-7 :-  Update the print statement below to give the user the correct word
            print(f"***************************IT WAS {chosen_word}! YOU LOOSE****************************") #print you Loose 

    if "_" not in display:
        game_over = True
        print("************************YOU WIN********************************") 

#------------------------------TODO-3 :- ------------------------------------------------------------------ 
#Print the ASCII art from the list stages that corresponds to the current number of Lives the user has remaining.

    print(stages[lives])