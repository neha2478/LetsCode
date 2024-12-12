#Create a List of Numbers 
# num_lst = [] #Empty String 
# n = int(input("Enter length for the List : "))
# for i in range(n):
#     a = float(input(f"Enter {i} element for List :"))
#     num_lst.append(a)

# print(num_lst)

#Creating a list of Strings 
# lst_str = []

# n = int(input("Enter the length of List : "))

# for i in range(n):
#     lst_str.append(input(f"Enter the {i} elemenet for List : "))
# print(lst_str)


#Accept any three string from one input() call
# n = int(input("Enter a no of strings u want to print :"))
# for i in range(n):
#     a = input(f"Enter the {i} string :")
#     print(f"The {i} string value : {a}")

#--------Using split()------------------
# str1, str2, str3 = input("Enter the string :").split() #here using the split method 
# print(f"The Name 1 : {str1}")
# print(f"The Name 2 : {str2}")
# print(f"The Name 3 : {str3}")

#---------use of Format specifier----------
# totalMoney = int(input("Enter total Amount :"))
# quantity = int(input("Enter the Quantity : "))
# price = int(input("Enter the price : "))

# print(f"I have {totalMoney} dollars so I can buy {quantity} football for {price} dollars.")

# print("I have {} dollars so I can buy {} football for {} dollars.".format(totalMoney, quantity, price))

#Geeks for Geeks questions
#1> Python Program to add two numbers.

# num1 = int(input("Enter the 1st no : "))
# num2 = int(input("Enter the second no : "))

# sum = num1 + num2
# print(f"The sum of {num1} & {num2} : {sum}")

#Find the maximum of two no :--
# num1 = int(input("Enter the 1st no : "))
# num2 = int(input("Enter the second no :"))

# if num2 > num1:
#     print(f"{num2} is maximum")
# else:
#     print(f"The {num1} is maximum")
'''
def findmaxfun(a,b):
    
    if a > b:
        return a
    else:
        return b

a = int(input("Enter value of a : "))
b = int(input("Enter value of b : "))

print(findmaxfun(a, b))

#else another way 
print(max(a, b))
print(a if a > b else b)
'''

# 3 :- Print The Factorial of a number 
#My Logic
# def factorial(n):
#     fact = 1
#     for i in range(n, 1, -1):
#         fact = fact * i
#     print(fact)
        
    
# num = int(input("Enter the a no :"))
# factorial(num)

#Another way to call function inside another function

# def fact(n):
#     if (n == 0 or n == 1):
#         return 1
#     else:
#         return n * fact(n - 1)
        
# num = int(input("Enter the a no :"))
# print(f"The factorial of {num} is {fact(num)}")

#Another logic using one liner 
# return 1 if (n == 0 or n == 1) else n * fact(n -1)

# 4> ---------FindSimple interst of
'''
def simpleInt(p, r, t):
    print('The principal is', p)
    print('The time period is', t)
    print('The rate of interest is',r)
        
    SI = (p * r * t) / 100
    return SI
    
    print(f"The Users simple intrest : {simpleInt(P, R, T)}")

def compondInt(p, r, t):
    #A -- amount
    #CI - Compound Intrest
    A = p*(1+(r/100))**t
    CI = A - p
    print(f"The Users Compound Intrest is {CI}")
    
P = int(input("Enter the principle amount :"))
R = int(input("Enter the rate :"))
T = int(input("enter the Time :"))

simpleInt(P, R, T) #Will Print Simple Intrest 
compondInt(P, R, T) #Will print Compound Intrest
'''

#Find Amstrong Number 
'''
def amstrong(n):
    copy = n
    sum = 0
    length = len(str(n)) # converting into string and than finding length
    while n > 0:
        rem = n % 10
        sum += rem ** length
        n = n // 10
    if copy == sum:
        print(f"It is a Amstrong no as {copy} = {sum}")
    else:
        print("Not a Amstrong!!")
        
num = int(input("Enter a number :"))

amstrong(num)
'''
#Area of a circle
'''
def area_circle(r):
    pi = 3.14
    
    return pi * r * r
    
radius = float(input("Enter a radius : "))

a = area_circle(radius)
print('%.2f'% a)
'''
#Python Program for Sum of squares of first n natural numbers
'''
def square_sum(n):
    sum = 0
    for i in range(1 , n + 1):
        sum += i * i
    return sum


num = int(input("Enter a number :"))
#calling the Function 
print(f"The result => {square_sum(num)}")
'''
#Using a formula of the above can do it
'''
def square_sum(n):
    return ((n * (n + 1) * (2 * n + 1 )) // 6) # using the direct formula 

num = int(input("Enter a number :"))
print(f"The result : {square_sum(num)}")
'''

#Prime No in an interval :-
'''
def check_Is_Prime(start_range , end_range):
    prime_no_lst = [] # List to store the prime no
    flag = 0 
    for i in range(start_range, end_range):
        for j in range(2, i):
            if(i % j == 0):
                flag = 1
                
                break 
            else :
                flag = 0
        if (flag == 0):
            prime_no_lst.append(i)
            
    return prime_no_lst
    
    
start_range = int(input("Enter  the Starting Range : "))
end_range = int(input("Enter the ending range : "))
#calling the function 
print(f"The List : {check_Is_Prime(start_range, end_range)}")
'''

#Here the another way to do it...
'''
def isPrime(start, end):
    prime_lst = []
    
    for i in range(start, end):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i/2)+1): # here the last range we can put i or int(i/2) + 1
                if (i % j == 0):
                    break
            else:
                prime_lst.append(i)
                
    return prime_lst

start = int(input("Enter the starting range : "))
end = int(input("Enter the ending range : "))

lst = isPrime(start, end) # storing it into a value

if (len(lst) == 0):
    print("There is no prime no in the range!!")
else:
    print(f"The prime no in range : {lst}")
    
'''

#Check waeather the no is prime or No

# num = 11
# Negative numbers, 0 and 1 are not primes
'''
if num > 1:
  
    # Iterate from 2 to n // 2
    for i in range(2, (num//2)+1):
      
        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")
'''

#Same using a function
'''
def isPrime(num):
    
    if num == 0 or num == 1:
        return False

    for i in range(2, int(num//2)+1):
        if num % i == 0:
            return False 
            
    return True 

num = int(input("Enter a no : "))
print(isPrime(num))
'''

#Another way using Flag 
'''
def isPrime(n):
    flag = 0
    if n == 0 or n == 1 :
        print(f"The {num} is not a Prime no !!")
    for i in range(2, n):
        if(n % i == 0):
            flag = 1
            break
    if(flag == 0):
        print(f"The {num} is a Prime no !!")
    else:
        print(f"The {num} is not a Prime no !!")
        
num = int(input("Enter a no : "))
isPrime(num)
'''

#Python Program for n-th Fibonacci number
'''
def fib(n):
    
    a = 0 # f1
    b = 1 # f2
    
    if n < 0:
        print("Incorrect Input from User")
    elif n == 0:
        return a
    elif n == 2:
        return b
    else:
        for i in range(2, n):
            c = a + b # f1 + F2
            a = b # f1 = f2
            b = c # f2 = f3
            
        return c
        
num = int(input("Enter a no : "))
print(fib(num))
'''

# To generate the fibonacci series to nth term -------------> Check with this no 
'''
def fib_series(num):
    
    print(f"Enter the value of nth perm : {num}")
    
    fib_lst = [] #Empty List
    
    a = 0
    b = 1
    c = 0
    cnt = 1
    
    print("Fibonacci series :", end = " ")
    while(cnt <= num):
        c = a + b
        fib_lst.append(c)
        cnt += 1
        a = b
        b = c
    return fib_lst
    
n = int(input("Enter a no : "))
print(fib_series(n))
'''

#To find ASCII value of a digit in Python 
#here we will use the ord() - converts into ASCII value
'''
char = input("Enter a charcter : ") #Enter a character

print(f"The ASCII vale of {char} : {ord(char)}")
'''

# Array Programs------------------
#Sum of arrays :-
'''
arr = []

ar_len = int(input("length of array : "))

for i in range(0,ar_len):
    b = int(input("Enter the value :"))
    arr.append(b)
    
print("The Array : ", end = " ")
print(arr)
'''

#Create your own array and find the sum of it using function calling 
'''
def create_array(arr, arr_len):
    
    for i in range(arr_len):
        user_input = int(input("Enter the value : "))
        arr.append(user_input)
    return arr
    
def sumOfarray(arr):
    s = 0
    for e in arr:
        s += e
    return s
    
#Find the largest element of array 
def maxEleArr(arr, arr_len):
    # return max(arr) 
    max = arr[0] # let us take the arbitrary value of max 
    
    for i in range(arr_len):
        if arr[i] > max:
            max = arr[i]
    return max
'''    
    
#To split acc to the index value not element
'''
def split_two(arr, n, k):
    arr1 = []
    arr2 = []
    for i in range(0,n):
        if i <= k:
            arr1.append(arr[i])
        else:
            arr2.append(arr[i])
            
    return arr2 + arr1
    
    
def find_remainder(arr, n ,j):
    
    #here we will find the reminder of multiplication of ele in array
    prod = 1
    
    for i in range(n):
        prod = prod * arr[i]
    
    return prod % j    
    
if __name__ == "__main__":
    arr = []  
    n = int(input("Enter the length of array : "))
    print(f"The Orignal Array : {create_array(arr, n)}")
    
    # k = int(input("The value u want to given :"))
    # print(f"Acc to element position vise : {split_add_Arr(arr, n, k)}")
    
    # print(f"Acc to index vise : {split_two(arr, n, k)}")
    
    j = int(input("Enter the Divider : "))
    
    print(f"The result i: {find_remainder(arr, n, j)}")
'''