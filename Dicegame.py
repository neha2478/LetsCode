from random import *

class Dicegame:

    def __init__(self , sides):
       self.sides = sides 

    #creating a function 
    def roll_dice(self):
        return randint(1, self.sides)
   

d1 = Dicegame(6)

print(d1.roll_dice())
print(d1.roll_dice())