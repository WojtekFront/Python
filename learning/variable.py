a= 10
b=10

a = [1,2,3]
b = [1,2,3]
print(a is b)
print(a == b)


a = [1,2,3]




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