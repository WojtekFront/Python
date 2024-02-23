secret_word = "one"
guess_word = input("Guess a word: ")
how_many_guesses = 3
guess_count = 0
out_of_guesses = False

while guess_word != secret_word and not (out_of_guesses):
    if guess_count < how_many_guesses:
        guess_word = input("Guess a word: ")
        guess_count += 1
    else:
        out_of_guesses = True
if not out_of_guesses:
    print("\n\nYou guessed the word!")
else:
    print("\n\nYou ran out of guesses!")

# first_value = 1

# while first_value <=10:
#     print(first_value)
#     first_value += 1

# print(first_value)