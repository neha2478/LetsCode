import random
stages = ['''
+---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
+---+
|   |
O   |
    |
    |
    |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]

#------------------------TODO-1 :- ------------------------------------------------------
# Create a variable called lives to keep track of the number of lives left.
# Set lives to equal 6
lives = 6 

chosen_word = random.choice(word_list) # here we will do a random choise rom list using choice fun of random module
print(chosen_word) #printing the chosen_word

placeholder = "" #variable with empty string
word_length = len(chosen_word) #len of chosen_word we are storing in a string word_length

for index in range(word_length): 
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a Letter: ").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display) 

#--------------------------------TODO-2 :- ----------------------------------------------------
# If guess is not a letter in the chosen_word, Then reduce lives by 1
#IF lives goes down to 0 then the game should end, and it should print "You Loose."
    
    if guess not in chosen_word:
        lives -= 1  # decrementing the value of lives
        #if lives is equal to 0 
        if lives == 0: 
            game_over = True # game over is true
            print("You Lose!!.") #print you Loose 

    if "_" not in display:
        game_over = True
        print("You Win!!.") 

#------------------------------TODO-3 :- ------------------------------------------------------------------ 
#Print the ASCII art from the list stages that corresponds to the current number of Lives the user has remaining.

    print(stages[lives])