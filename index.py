#------------------------------------------------------------------------------
# retun informations
def multiply(a, b):
    if isinstance(a,(int,float)) and isinstance(b,(int,float)):
        a = float(a)
        b = float(b)
        c = a * b
    else:
        c = "Not a number"
    return c

print( multiply(7, 2))
print( multiply(2, "word"))

#------------------------------------------------------------------------------
# learning functions and parameters
# name = input("Enter your name: ")
# name = "Michael"
# message = "How's your daily goal?"

# def say_hi(name, message):
#     print("\n\n----------------")
#     print("Hi, " + name + "!")
#     print(message)
#     print("----------------\n\n")
    
# say_hi(name, message)

#------------------------------------------------------------------------------
# 1:20
# tupple 
# coordinates = [(1,2), (3,4), (5,6), (7,8),]
# print(coordinates[0])

#------------------------------------------------------------------------------
# friends = ['John','Andrew','Tom','Gregory']
# lucky_numbers = [1,2,3,4,5,6,7,8,22,23,24,25,26,27,28]
# friends.insert(3, "Joohn")
# friends.extend(lucky_numbers)
# print(friends.count(1))
# print(friends.index('John'))
# friends.sort() - not mix numbers with strings
# friends[0] = 'Michael'
# friends.append('friends')
# print(friends)
# friends.remove('Andrew')  
# print(friends)
# friends.pop(0) 
# print(friends)
# friends.reverse()
# print(friends)

#------------------------------------------------------------------------------
# Mad Libs Game
# color = input("Enter a color: ")
# plural_noun = input("Enter a plural noun: ")
# celebrity = input("Enter a celebrity: ")

# print("\n\nRoses are " + color)
# print(plural_noun + " are blue")
# print("I love " + celebrity)

#------------------------------------------------------------------------------
# num1 = float(input("Enter the first number:"))
# num2 = float(input("Enter the second number:"))
# result = num1 + num2
# print(result)

#------------------------------------------------------------------------------
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# print("Hello, " + name + "! You are " + str(age) + " years old.")

#------------------------------------------------------------------------------
# from math import *

# character_word = 'Magic'
# print('Hello '+ character_word.upper() +' world')
# print('hello '+ character_word.upper() +' world')
# print('this world is really '+ character_word.lower() +' awesome')
# print('I am born to create some cool stuff')
# print('So, I am '+ character_word +' rules that')

