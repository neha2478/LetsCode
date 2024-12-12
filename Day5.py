#Understanding Loops in python
'''
fruits = ["Apple", "Banana", "Pear","Strawberry", "Guava"]
for f in fruits:
    print(f)
    print(f + "pie")
    print(fruits)
'''

#Challenge Find Highest Score
'''
student_score = [150, 142, 105, 120, 171, 149, 24, 59, 68, 199, 78, 89]

total_exam_score = sum(student_score)
print(f"Total Exam Score is : {total_exam_score}")
'''

#Another way of adding the values ...
#Using For Loop
'''
sum = 0
for score in student_score:
    sum += score
print("The Sum of all the score is : {}".format(sum))
'''

#To print the largest no in the List of scores
# from param import Range


# print(f"The Largest score is : {max(student_score)}")

#To print each no of student_score List
'''
for s in student_score:
    print(s)
'''

'''
max_score = 0
for score in student_score:
    if score > max_score:
        max_score = score

print(max_score)
'''

#for loop and the range() function 
# fruits = ["Apple", "Peach", "Pear"]

# for f in fruits:
#     print(f)


#Range Function :-
# It will help to print values in Range...
'''
Example :- 
for num in range(a, b):
    print(num)
'''
# Range Function with for Loop
'''
for number in range(1, 11):
    print(number)
'''
'''
total = 0
for number in range(1, 10):
    total += number 
print(total)
'''