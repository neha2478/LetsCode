# Picking a Random Words and Checking Answers :-

# word_List = ["aardvark", "baboon", "camel"]

'''
TODO-1 :- Randomly choose a word from the word _List and assign it to a variable called chosen_word. Then print it.

TODO-2 :- Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase

TODO-3 :- Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it is "Wrong if it's not.
'''

# Solution of TODO-1
import random
word_List = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_List)
print(chosen_word)

#Solution of TODO-2
guess = (input("Guess a letter : ")).lower()
print(guess)

#Solution of TODO-3
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")