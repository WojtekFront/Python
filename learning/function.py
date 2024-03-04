import sys ,time, string

char_list = list(string.ascii_letters)
char_tuples = tuple(string.ascii_letters)
char_set = set(string.ascii_letters)

def membershiop_test(n, container):
    for i in range(n):
        if 'z' in container:
            pass

start = time.perf_counter()
membershiop_test(10000000, char_list)
end = time.perf_counter()
print("time for characters list: " + str(end - start))

# start = time.perf_counter()
# membershiop_test(10000000, char_tuples)
# end = time.perf_counter()
# print("time for characters tuple: " + str(end - start))

# start = time.perf_counter()
# membershiop_test(10000000, char_set)
# end = time.perf_counter()
# print("time for characters set: " + str(end - start))









# -----------------------------------------------------------------------------
# def compare_using_equals(n):
#     a = "a long string that is not interned" * 200
#     b = "a long string that is not interned" * 200
#     for i in  range(n):
#         if a == b:
#             pass

# def compare_using_interning1(n):
#     a = sys.intern("a long string that is not interned" * 200)
#     b = sys.intern("a long string that is not interned" * 200)
#     for i in  range(n):
#         if a == b:
#             pass


# def compare_using_interning2(n):
#     a = sys.intern("a long string that is not interned" * 1000)
#     b = sys.intern("a long string that is not interned" * 1000)
#     for i in  range(n):
#         if a is b:
#             pass

# start = time.perf_counter()
# compare_using_equals(1000000)
# end = time.perf_counter()

# print(end - start)

# start = time.perf_counter()
# compare_using_interning1(1000000)
# end = time.perf_counter()

# print(end - start)

# start = time.perf_counter()
# compare_using_interning2(1000000)
# end = time.perf_counter()

# print(end - start)



# a = sys.intern("hello world")
# b  = sys.intern('hello world')

# print(id(a), id(b))
# print(a is b)

# -----------------------------------------------------------------------------
# def square(a):
#     return a ** 2

# def cube(a):
#     return a ** 3

# def select_function(fn_a):
#     if fn_a == 1:
#         return square
#     else:
#         return cube

# f = select_function(2)
# f is cube
# f(2)


# def exec_function(fn,n):
#     return fn(n) 
# print(select_function(1)(3))
# # print(exec_function(square,10))