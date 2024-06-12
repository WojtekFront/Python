from functools import reduce

l = [0, 5, 6, 7, 8, 9, 10, 11, 12, 13,4, 40, 50, 60, 70, 8, 8, 2, 1, 2]

# print(reduce(lambda a,b: a if a>b else b,l))
# print(sum(l))
# print(reduce(lambda a, b: bool(a) or bool(b),l))
# print(reduce(lambda a, b: a*b , l))




# l = [1,15,8,6,10,9]
# max_value = lambda a,b: a if a>b else b

# # def max_sequence(sequence):
# #     result = sequence[0]
# #     for e in sequence[4:]:
# #         result = max_value(result, e)
# #     return result

# # print(max_sequence(l))

# min_value = lambda x,y: x if x<y else y
# # def fun_min(new_value):
# #     result = new_value[0]
# #     for e in new_value[1:]:
# #         result = min_value(result, e)
# #     return result

# # print(fun_min(l))

# add = lambda a,b:a+b
# def _reduce(fn,sequence):
#     result = sequence[0]
#     for e in sequence[1:]:
#         result = fn(result, e)
#     return result

# print(_reduce(min,l))
# print(_reduce(max,l))
# print(_reduce(add,l))
