# -----------------------------------------------------------------------------
# lambda x: x**2
new_lambda = lambda x: 5 + x
# print(new_lambda(2))

def apply_lambda(x,fn):
    return fn(x)

print(apply_lambda(4,new_lambda))




# -----------------------------------------------------------------------------
# def new_func(a: 'value a')-> 'output from annotation':
#     """Descriptions for new functions"""
#     print(a)

# print(new_func.__doc__)
# print(new_func.__annotations__)

# -----------------------------------------------------------------------------
# def learn(a: str, b: str)->str:
#     "describe"
#     return a + b
# print(learn(False,2))
# learn(1,2)
# class Test:
#     """123"""
#     print(Test.__doc__)

# -----------------------------------------------------------------------------
# cache = {}
# def factorial(n, cache={}):
#     """opis def
#     druga linia 
#     trzecia linia
#     czwarta linia
#     """
#     if n < 1:
#         return 1
#     elif n in cache:
#         return cache[n]
#     else:
#         print("calculating {0}!".format(n))
#         result = n * factorial(n-  1, cache = cache)
#         cache[n] = result
#         return result

# print(factorial.__doc__)

# def factorial(n):
#     if n < 1:
#         return 1
#     else:
#         print("calculating {0}".format(n))
#         return factorial(n-  1)
    
# factorial(2, cache) 
# print(cache)



# -----------------------------------------------------------------------------
# def add_item(name, quantity, unit, grocery_list=[]):
#     grocery_list.append("{0} ({1} {2})".format(name, quantity, unit))
#     return grocery_list

# store1 = []
# store2 = []
# store1 = add_item('banas', 2, "kg")
# add_item('milk', 3, "litr")
# add_item('banas', 2, "kg")
# store2 =add_item('milk', 3, "litr")

# print(store1)
# print(store2)

# -----------------------------------------------------------------------------
# my_list =[1,2,3]
# def func(a=my_list):
#     print(a)
# # func(['a','b'])
# my_list.append(0)

# func()

# -----------------------------------------------------------------------------
# def calc_hi(*args, log_to_console = False):
#     hi = int(bool(args)) and max(args)
#     lo = min(args) if len(args) > 0 else 0
#     avg = (hi + lo) / 2

#     if log_to_console:
#         avg ="high={0}, low={1}, avg={2}".format(hi,lo,avg)
#         return avg
#     return avg

# avg = calc_hi(1,2,3,100)
# print(avg)
# avg2= calc_hi(1,2,3,100, log_to_console=True)
# print(avg2)

# def func(d=1,a=2, b=3):
#     print(d + a + b)

# def func1(**kwargs):
#     print(" func1{0}".format(kwargs))

# def func2(*args, **kwargs):
#     print(" func2{0}".format(args))
#     print(" func2{0}".format(kwargs))
#     # print("tekst")

# func(1,2,3)

# func1(a=1, b=2, c=3)

# func2(1,2,3,4,5,6,7,8,a=9,b=10)
    

# -----------------------------------------------------------------------------
# def func1(a, b, *args, d=20, e):
#     print(a)
#     print(b)
#     print(args)
#     print(d)
#     print(e)

# func1(1,2,3,4, d=25, e=22)

# -----------------------------------------------------------------------------
# *args

# list_func = [10,11,12]
# def new_args(*args):
#     if args:
#         print([*args])


# # def new_args(a,b=10, *c):
# #     print(a)
# #     print(b)
# #     if c:
# #         print(c)

# new_args(5,10,10,10,10,10,10)
# new_args(*list_func)

# -----------------------------------------------------------------------------
# s1 = "abc"
# s2 = "def"
# s3 = [*s2, *s1]

# print(s3)

# s = "python"
# a,b,c,d=s[0],s[1],s[2:-1],s[-1]

# print(a)
# print(b)
# print(c)
# print(d)

# l = [1,2,3,4,5,6,7,8,9,10]
# a = l[0]
# b = l[1:]

# print(a)
# print(b)
# a, *b = l
# print(l)
# -----------------------------------------------------------------------------
# iterations

# a,c,d,e, *b = [-10, 5, 2, 100]
# print(a)
# print(b)

# a_tuple = (1,2,3,4,5,6,7,8,9)
# b_list = [1,2,3,4,5,6,7, 8, 9] 
# c_sets = {1,2,3,4,5,6,7,8,9, 10,11,12,13,14,15,16,17}
# d_dictionaries = {'a': "text1",'b': "text2", 'c': "text3"}

# for a,b in d_dictionaries.items():
#     print('key={0}, value={1}'.format(a,b))

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