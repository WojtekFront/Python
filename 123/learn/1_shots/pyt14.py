# In this simple exercise, you will create a program that will take two lists of integers, a and b. Each list will consist of 3 positive integers above 0, representing the dimensions of cuboids a and b. You must find the difference of the cuboids' volumes regardless of which is bigger.
# For example, if the parameters passed are ([2, 2, 3], [5, 4, 1]), the volume of a is 12 and the volume of b is 20. Therefore, the function should return 8.
# Your function will be tested with pre-made examples as well as random ones.
# If you can, try writing it in one line of code.
import math
def find_difference(a, b):
    return math.prod(a) - math.prod(b)

def find_difference(a,b):
    var_a = 1
    var_b = 1
    for i in range(3):
        var_a *= a[i]
        var_b *= b[i]
    return abs(var_a - var_b)

def find_difference(a,b):
    A = B = 1
    for i, j in zip(a,b):
        A *= i
        B *= j
    return abs(A - B)

print(find_difference([1,1,1],[1,2,4]))