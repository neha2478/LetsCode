import random
word_list = ["aardvark", "baboon", "camel"] #word list

chosen_word= random.choice(word_list) # choose a random word from List with the help of choice() from random module
print(chosen_word) # printing the above

#---------TODO-1: Create a "placeholder" with the same number of black as the chosen_word-------------------------------------
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_" 
print(placeholder)

#--------------------------------TODO-1:- Use a while Loop to let the year guess again.--------------------------------

game_over = False # type: ignore

correct_letters = []

while not game_over: # type: ignore
    guess = input("Guess a letter: ").lower() #guessing a input and converting it into lower case using lower() storing it into guess
    
    display = "" # creating a variable to display output in which we are storing empty string

    #----------------TODO-2:- Change the for Loop so that you keep the previous correct letters in display.------------------------

    #for Loop with a range of chosen_word
    for letter in chosen_word:
        #if letter is equal to guess
        if letter == guess:
            display += letter # it will be added to display
            correct_letters.append(letter) # as the guess == letters so we can put anyone in argument of append()
            # will be appended to the correct_letter list 
        
        #if letter is in correct_letter List
        elif letter in correct_letters:
            display += letter  # we will add space
        
        else:
            display += "_" # if none of the letter we guess is matching adding underscore on that index

    print(display)  # printing Display      

    #if underscore is not there in display string 
    if "_" not in display:
        game_over = True # game is over --> True
        print("You Win!!") #print You Win.