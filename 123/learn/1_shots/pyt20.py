# You are given two interior angles (in degrees) of a triangle.
# Write a function to return the 3rd.
# Note: only positive integers will be tested.
# https://en.wikipedia.org/wiki/Triangle

def other_angle(a, b):
    if not(isinstance(a,(int,float)) or isinstance(b, (int, float))):
        raise ValueError("Kąty muszą być liczbami.")
    if a<=0 or b<=0:
        raise ValueError("Kay w trójkącie muszą być dodatnie")
    return 180 - a -b

print(other_angle(10,10))