#Create a class of Student 

#Student Challenge
'''
class Book
title
author
price

show_details()
'''

class Book:
    
    #constructor of class
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
        
        
    def show_details(self):
        print('Title of the book ', self.title)
        print('Title of the book ', self.author)
        print('Title of the book ', self.price)

#creating an object of class Book , store it in a reference variable    
b1 = Book('Python Crash Course' , 'Shruti Karmakar', 1000)
b1.show_details()

b2 = Book('Python Crash Course' , 'Kundan Saha', 700)
b2.show_details()