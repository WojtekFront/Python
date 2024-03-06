
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
import decimal
from decimal import Decimal
import math


# Decimal.getcontex().prec=0























# x= Decimal(10)
# y = Decimal(3)
# print(divmod(x,y))
# # help(Decimal)
# a = Decimal('1.5')
# print(a.ln())
# print(a.exp())
# print(math.sqrt(a))

# ------------------------------------------------------------------------------
# import math 
# x = 0.1 + 0.1 + 0.1
# xy = float(format(x, '.30f'))
# print(xy)
# print(round(xy,3))

# a= 10000.12423543245635645744563842384257828472448234
# b= 10000.12742354324564435645744563842384257828472448234

# print(a)
# print(type(a))
# print(math.isclose(a,b, rel_tol=1e-5, abs_tol=1e-5))

# -----------------------------------------------------------------------------
# print(format(0.1, '.30f'))

# -----------------------------------------------------------------------------
# from fractions import Fraction
# import sys

# print(Fraction(denominator = 2, numerator = 3))
# print(Fraction('22/7'))

# a = Fraction(22,7)
# a = a.limit_denominator(4)
# print(float(a))

# b= 11
# print(sys.getsizeof(a))
# print(sys.getsizeof(b))
# print(float(a + b))

# -----------------------------------------------------------------------------
# import fractions

# a = fractions.Fraction(22,9)
# print(a)
# print(float(a))
# print(int(a))

# -----------------------------------------------------------------------------
# n = 100
# b = 3 

# value = ( n // b ) * b + n % b 

# print(n % b)
# print(value)


# num_val = int("1010", base=8)
# num_val1 = int("1010", base=10)
# print(bin(num_val1))
# print(oct(num_val1))
# print(hex(num_val1))

# -----------------------------------------------------------------------------
# import sys

# print(sys.getsizeof("bla blaz bla bla"))
# print(sys.getsizeof(1))

# -----------------------------------------------------------------------------
# def my_func(self):
#     return self

# def cube(fn_a):
#     return fn_a ** 3

# def select_function(fn_a):
#     if fn_a > 0:
#         return cube(fn_a)
#     else:
#         return 0

# select_function(2)(3)

# f=select_function(2)
# print(f is select_function(2))
# print(f == select_function(2))
# print(f)
# print(f is 4)
# print(f == 4)

# print(cube(3)
#       )
# print(my_func(1))

# help(my_func(1))

# -----------------------------------------------------------------------------
# a= 10
# b=10

# a = [1,2,3]
# b = [1,2,3]

# a = 10
# b= 10.0
# print(a is b)
# print(b is a)
# print(a == b)

# Garbage Collection
# import ctypes
# import gc

# def ref_count(address):
#     return ctypes.c_long. from_address(address).value

# def object_by_id(object_id):
#     for obj in gc.get_objects():
#         if id(obj) == object.id:
#             return print("object exists")
#     return print("object does not exist")

# class A:
#     def __init__(self):
#         self.b = B(self)
#         print(ref_count(self.b))

# refernce counting
# import sys

# my_variable = 10
# sys.getrefcount(my_variable)
# print(sys.getrefcount(my_variable))




# Variables and memory references
# a = 10
# print(id(a))
# print(hex(id(a)))