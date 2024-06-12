import sys

word_0 = ""
word_1 = "    aaaaRyba     "
word_2 = "aByraaaa"
word_3 = "krowa"
word_4 = "aByraaaa"
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
        elif len(f_word) > 0 and len(s_word) > 0 and len(f_word) == len(s_word): 
                word_len = len(f_word)
                compare_letter_in_words(f_word, s_word, word_len)
        else:
            print((f"words is not ok"))
            sys.exit(0)
    except:
        print((f"words do not match, error"))
        sys.exit(1)

# learnindg solutions
def compare_letter_in_words(f_word, s_word, word_len):
    f_list = sorted(list(f_word.lower()))
    s_list = sorted(list(s_word.lower()))
    answear = "words same"
    for i in range( word_len):
        if f_list[i] != s_list[i]:
            answear = "words do not match"
            break
    print(answear)

# the best solutions        
def compare_words(f_word, s_word):
     try:
        if f_word == s_word:
            print("words match")
        else:
            print("words do not match")
     except:
        print("words do not match, error")
        
# test example
# existing_words(word_0, word_1)
# existing_words(word_2, word_6)

existing_words(word_1, word_4)
# existing_words(word_1, word_4)
# existing_words(word_3, word_5)


