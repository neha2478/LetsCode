# Class for Circle
'''
Write a class for circle:
    radius
    area()
    perimeter
    
    area :- pi * radius * radius
    perimeter :- 2 * pi * radius
'''

#Writing the class

#Importing the math function
import math 

class Circle:
   
   #constructor of the Circle
    def __init__(self, radius):
       self.radius = radius
    
    def area(self):
        return math.pi * self.radius   

    def perimeter(self):
        return  2 * math.pi * self.radius

#calling the Function
c1 = Circle(23) #creating the object and storing in reference variable 
print(c1.area())
print(c1.perimeter())

c2 = Circle(78)
c2.radius = 67
print(c2.area())
print(c2.perimeter())

