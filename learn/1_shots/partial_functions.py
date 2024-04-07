from functools import partial
# -----------------------------------------------------------------------------
def pow(base, exponent):
    print( base ** exponent)

square = partial(pow, exponent=2)
cube = partial(square, exponent=3)
square(3)
cube(3)
cube(base=6, exponent=6)












# -----------------------------------------------------------------------------
# def my_new_func(a,b,c):
#     print(a,b,c)

# f = lambda b,c: my_new_func(10,b,c)
# # f(7,2)

# f_p= partial(my_new_func, 1,22)
# f_p(333)

