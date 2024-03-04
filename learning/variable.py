

num_val = int("A13F", base=16)
print(num_val)

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
a = 10
# print(id(a))
# print(hex(id(a)))