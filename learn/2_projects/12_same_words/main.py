import sys

word_0 = ""
word_1 = "    Ryba     "
word_2 = "piesek"
word_3 = "krowa"
word_4 = "ryba"
word_5 = "krowa"
word_6 = None
words_list = [word_1, word_2, word_3, word_4, word_5]

"""
A. same words
   + 1. check if existing two words and length is bigger then zero
   + 2. trim words and check length
    3. take element from one list and compare to element from another list

"""

def existing_words(f_word, s_word):
    try:

        # trim words
        f_word = f_word.strip()
        s_word = s_word.strip()

        # check if existing two words and length is bigger then zero
        if not (f_word and  s_word):
            print((f"incorrect word"))
            # sys.exit(0)
        elif len(f_word) > 0 and len(s_word) > 0: 
                compare_words(f_word, s_word)
        else:
            print((f"words is not ok"))
            # sys.exit(0)
    except:
        print((f"words do not match, error"))
        # sys.exit(1)

def compare_words(f_word, s_word):
     try:
        if f_word == s_word:
            print((f"words match"))
        else:
            print((f"words do not match"))
     except:
        print((f"words do not match, error"))
        # sys.exit(1)



# test example
# existing_words(word_0, word_1)
# existing_words(word_2, word_6)

existing_words(word_1, word_2)
existing_words(word_1, word_4)
existing_words(word_3, word_5)


