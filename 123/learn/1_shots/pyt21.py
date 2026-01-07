# Create a function that accepts a string and a single character, and returns an integer of the count of occurrences the 2nd argument is found in the first one.

# If no occurrences can be found, a count of 0 should be returned.

# ("Hello", 'o')  =>  1
# ("Hello", 'l')  =>  2
# ("", 'z')       =>  0
# Notes
# The first argument can be an empty string
# In languages with no distinct character data type, the second argument will be a string of length 1

def str_count(string, letter):
    # lenS = len(string)-1
    # count = 0

    # while 0 <= lenS:
    #     if string[lenS] == letter:
    #         count += 1
    #     lenS = lenS -1

    # return count
    # return string.count(letter)
    count = 0
    for char in string:
        if char == letter:
            count +=1

    return count


print(str_count("rabarbar","a"))

print(str_count("mama","m"))