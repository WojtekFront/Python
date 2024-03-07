
# ------------------------------------------------------------------------------
# boolean

a = bool(1)
b = True
c = [""]



print()
print(bool(c))
# print(False == 0)
# print(int(a))
# print(a == b)
# print(issubclass(bool, int))

# ------------------------------------------------------------------------------
# Complex numbers
# import cmath

# a = complex(1, 2)
# a =0.1j
# b = 1 + a
# c = 1 + 0.1j
# d = cmath.phase(c)
# e = 1.01j

# print(a)
# print(1 + a)
# print(b)
# print(c)
# print('d: {d}'.format(d))

# print(a + a)
# print(a * a)
# print((a - a ) * a)

# task x**2+4=0
# import cmath
# a = 1
# b = 0
# c = 4

# delta = (b**2) - (4 * a * c)

# root1 =(-b - cmath.sqrt(delta)) / (2 * a)
# root2 = (-b + cmath.sqrt(delta)) / (2 * a)
# print(delta)
# print(f" Pierwiaski rwnania x^2 + 4 = 0 to {root1} + {root2} = 0")

# import numpy  as np

# a = complex(1, 2)
# b = 3 +4j
# matrix_a = np.array([[2 + 3j, 1-2j], [0.5 + 1j, -2]])
# matrix_b = np.array([[1 - 1j, 2 + 2j], [3j, 4]])

# print(float(a))
# print(float(b.real + b.imag))

# ------------------------------------------------------------------------------
# import decimal
# from decimal import Decimal
# import math, sys
# import time

# def run_float(n=1):
#     a = 3.1415
#     for i in range(n):
#        math.sqrt(a)

# def run_decimal(n=1):
#     a = Decimal('3.1415')
#     for i in range(n):
#         a.sqrt() 

# n = 5000000

# start = time.perf_counter()
# run_float(n)
# end = time.perf_counter()
# print('float: ', end-start)

# start = time.perf_counter()
# run_decimal(n)
# end = time.perf_counter()
# print('Decimal: ', end-start)

# a = 3.1415
# b = "3.1415"
# c = Decimal("3.1415")

# print(sys.getsizeof(a))
# print(sys.getsizeof(b))
# print(sys.getsizeof(c))

# print(format(a, '1.27f'))
# print(format(float(b), '1.27f'))
# print(format(float(round(float(b),4)), '1.27f'))
# print(format(c, '1.27f'))

# print(format(round(float(b),4), '1.27f'))
# help(round)

# x= 2
# x_dec = Decimal(2)

# root_float = math.sqrt(x)
# root_mixed = math.sqrt(x_dec)
# root_dec = x_dec.sqrt()

# # print(format(root_float, '1.27f'))
# # print(format(root_mixed, '1.27f'))
# # print(format(root_dec, '1.27f'))

# print(format(root_float * root_float, '1.27f'))
# print(format(root_mixed * root_mixed, '1.27f'))
# print(format(root_dec * root_dec, '1.27f'))

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