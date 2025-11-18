# If you can't sleep, just count sheeps!!

# Task:
# Given a non-negative integer, 3 for example, return a string with a murmur: 
# "1 sheep...2 sheep...3 sheep...". Input will always be valid, i.e. no negative integers.

def count_sheep(n):
    long_text = ""
    x=0
    while x< n:
        x += 1
        long_text = long_text + str(x) + " sheep..."
    return long_text
    


print( count_sheep(1))