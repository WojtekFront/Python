# Create a function with two arguments that will return an array of the first n multiples of x.
# Assume both the given number and the number of times to count will be positive numbers greater than 0.
# Return the results as an array or list ( depending on language ).
# Examples
# x = 1, n = 10 --> [1,2,3,4,5,6,7,8,9,10]
# x = 2, n = 5  --> [2,4,6,8,10]

def count_by(x, n):
    array = []
    y = 1
    while n >= y:
        array.append(x*y)
        y+=1
    return array

def count_by2(x,n):
    array = []
    for i in range( 1, n + 1):
        array.append(x * i)
    return array

print(count_by2(2,5))
