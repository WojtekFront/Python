# Write a function that accepts a non-negative integer n and a string s as parameters, and returns a string of s repeated exactly n times.

# Examples (input -> output)
# 6, "I"     -> "IIIIII"
# 5, "Hello" -> "HelloHelloHelloHelloHello"

def repeat_str(repeat, string):
    # newstring = ""
    # while repeat >0:
    #     newstring = newstring + string
    #     repeat = repeat -1
    # return newstring
    # return string * repeat
    return "".join([string] * repeat)

print(repeat_str(5,"a"))


print(repeat_str(5,"tornado wieje dość mocno"))