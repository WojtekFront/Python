
# -----------------------------------------------------------------------------
# iterations
a_tuple = (1,2,3,4,5,6,7,8,9)
b_list = [1,2,3,4,5,6,7, 8, 9] 
c_sets = {1,2,3,4,5,6,7,8,9, 10,11,12,13,14,15,16,17}
d_dictionaries = {'a': "text1",'b': "text2", 'c': "text3"}

for a,b in d_dictionaries.items():
    print('key={0}, value={1}'.format(a,b))

# for i in c_sets:
#     print(i)

# for d_key in d_dictionaries.values():
#     print(d_key)

# d_dictionaries = {'a': "text1", 'b': "text2", 'c': "text3"}

# for d_key in d_dictionaries:
#     formatted_text = "value is {0}".format(d_dictionaries[d_key])
#     print(formatted_text)

# hmm = [a,b,c,d] =[1,2,3,4] # ugly

# for e in hmm:
#     print(e)
# print(type(a))
# print(b)
# print(c)
# print(d)

# -----------------------------------------------------------------------------
# a = b = c = 2 
# b = 5
# c = 3
# def test_variables(a, b=1, c=2):
#     print('a= {0}, b= {1}, c= {2}'.format(a, b, c))
#     print('a= {a}, b= {b}, c= {c}'.format(a=a, b=b, c=c))

# test_variables(a,b,c)

# -----------------------------------------------------------------------------
# Keywords Aruments
# def my_fubc(a=0, b=0, c=0, d=0 ):
#     return a + b*10 + c*100 + d*1000

# print(my_fubc(1, 2, d=3))

# -----------------------------------------------------------------------------
# import sys ,time, string

# char_list = list(string.ascii_letters)
# char_tuples = tuple(string.ascii_letters)
# char_set = set(string.ascii_letters)

# def membershiop_test(n, container):
#     for i in range(n):
#         if 'z' in container:
#             pass

# start = time.perf_counter()
# membershiop_test(10000000, char_list)
# end = time.perf_counter()
# print("time for characters list: " + str(end - start))

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