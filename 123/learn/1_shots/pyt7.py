# Complete the solution so that it reverses the string passed into it.
# 'world'  =>  'dlrow'
# 'word'   =>  'drow'

def solution(string):
    reverse = list(string)
    reverse.reverse()
    reverse = ''.join(reverse)
    return reverse

def solution2(string):
    return string[7:1:-1]

def solution3(string):
    reverse = ""
    for char in reversed(string):
        reverse += char
    return reverse

print(solution2("bla2 b22laa"))