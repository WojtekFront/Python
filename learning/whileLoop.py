a = 0
while a <= 4:
    
    print("{0}".format(a))
    a += 1

# -----------------------------------------------------------------------------
# l = [1, 2, 3]
# val = 10

# found = False
# idx = 0
# print("\n\n")
# while idx < len(l):
#     if l[idx] == val:
#         found = True
#         break
#     idx += 1

# if not found:
#     l.append(val)

# print(l)

# -----------------------------------------------------------------------------
# a = 0
# while a <= 10:
#     a += 1
#     if a % 2 == 0:
#         continue
#     print(a)

# -----------------------------------------------------------------------------
# import re
# while True:
#     name = input("Enter your name: ")
#     if re.match("^[a-zA-Z]+$", name):
#         break
#     else:
#         print("Please enter a valid name")

# print("Hello, " + name)

# -----------------------------------------------------------------------------
# min_lenght = 2
# name = ""
# while True:
#     name = input("Enter your name: ")
#     if name:
#         break
#     else:
#         print("Please enter a valid name")

# print("Your name is {name}".format(name=name))    

# while not(len(name) >= min_lenght and name.isprintable() and name.isalpha()):

# -----------------------------------------------------------------------------
# my_value = 0

# while True:
#     print(my_value)
#     my_value += 1
#     if my_value >= 10:
#         print("\n Good Job")
#         break

# -----------------------------------------------------------------------------
# my_value = 0
# while my_value <= 10:
#     print(my_value)
#     my_value += 1

#------------------------------------------------------------------------------
# secret_word = "one"
# guess_word = input("Guess a word: ")
# how_many_guesses = 3
# guess_count = 0
# out_of_guesses = False

# while guess_word != secret_word and not (out_of_guesses):
#     if guess_count < how_many_guesses:
#         guess_word = input("Guess a word: ")
#         guess_count += 1
#     else:
#         out_of_guesses = True
# if not out_of_guesses:
#     print("\n\nYou guessed the word!")
# else:
#     print("\n\nYou ran out of guesses!")

# first_value = 1

# while first_value <=10:
#     print(first_value)
#     first_value += 1

# print(first_value)