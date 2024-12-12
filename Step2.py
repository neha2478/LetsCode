# Step 2:- Replacing Blanks with Guesses
#Solution
import random
word_list = ["aardvark", "baboon", 'camel']

chosen_word= random.choice(word_list)
print(chosen_word)

#TODO-1: Create a "placeholder" with the same number of black as the chosen_word  
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_" 
print(placeholder)

#TODO-2 : Create a "display" that puts the guess in the right position and _ in the rest of the string.
#Solution 
display = ""

guess = (input("Guess a letter : ")).lower()
print(guess)

for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += "_"
print(display)