# In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

# Example
# filter_list([1,2,'a','b']) == [1,2]
# filter_list([1,'a','b',0,15]) == [1,0,15]
# filter_list([1,2,'aasf','1','123',123]) == [1,2,123]

def filter_list(l1):
#   result =[]
#   for x in l1:
#     if isinstance(x,int):
#         result.append(x)
#     return result
    return [x for x in l1 if isinstance(x,int)]

print(filter_list([1,2,"pewna pani miała psa", 3,4,"pies ten dziwne miał maniery"]))