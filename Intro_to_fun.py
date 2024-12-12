# here we will learn how to create a function.
'''
def my_function():
	#Do this
	#Then do this 
	#Finally do this
     
my_function()
'''
#Example
'''
def greet():
    print("Hello")
    print("How do you do?")
    print("Isn't the weather nice?")

#To call the function
greet()
greet()
'''

# Functions with Inputs 
'''
def my_function():
    #Do this with 123
    # #Then do this
    # #Finally do this 

my_function()
'''
#Functions that allows for inputs 
'''
def greet_with_name(name):
    print(f"Hello {name}") #Using F string 
    print(f"How do you do {name}?")

greet_with_name("Angela") # calling the function along with passing the parameter.
'''

#If we want to the same with user Input
'''
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")

a = input("Enter a name: ")
greet_with_name(a)

'''

#The value that we pass in  while calling a function,Is called a Argument
# a -> argument
# name -> parameter

#----------- Lecture 62:- POSITIONAL vs. KEYWORD ARGUMENTS------------------------

#Functions with more than 1 input.

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with("Neha", "Bud Bud")

greet_with("Bud Bud","Shruti")


#Understanding Positional arguments :-

greet_with(name="Angela", location= "London")