# -----------------------------------------------------------------------------
digits_list = [22, 11, 21, 45, 21, 45, 12, 21, 45, 21, 19, 45, 21]
string_list = ["first_word", "second_word", "third_word", "fourth_word", "fifth_word", "sixth_word"]
string_list_u = ["first_word", "Second_word", "third_word", "Fourth_word", "fifth_word", "Sixth_word"]
new_list = [*digits_list,*string_list]
new_list2 = [digits_list, string_list]
values_string = "abcdefghijklmnopqrstuvwxyzABCDEFGH"
tuple_element = ("kiwi", "orange")




print(dir(list))






# newest_list = string_list.copy()
# newest_list2 = string_list.copy()
# newest_list3 = string_list.copy()

# string_list.insert(0,"11")
# newest_list2.append("11")

# print(string_list)
# print(newest_list)
# print(newest_list2)
# print(newest_list3)
# print(string_list)
# print(digits_list)

# print(string_list_u)
# string_list_u.sort(key = str.lower)

# string_list.reverse()
# digits_list.sort(reverse=True)

# def my_func(n):
#     return abs(n-50)
# print(digits_list)
# digits_list.sort(key = my_func)

# newest_list = [x for x in string_list if len(x)>10]
# newest_list = [x for x in range(10) if x%2==0]
# newest_list = [x.upper() for x in string_list
# newest_list = ['ello' for  x in string_list]
# print(newest_list)

# [print(x)for x in string_list]
# digits_list.clear()
# del string_list, digits_list
# for i in range(len(string_list)):
#     print(string_list.pop(-1))
# for i in digits_list:
#     if i == 21:
#         digits_list.remove(i)

# print(string_list)
# print(digits_list)

# string_list[0] = 2
# string_list.insert(0, "abcdefghij")
# string_list.append("something")
# string_list.extend(tuple_element)

# print(string_list)

# for i in digits_list:
#     if i == 21:
#         print("21 in digits_list") 

# print(string_list[2:])
# for i in string_list:
#     print(i[-2:])
# print(values_string[-2:])

# print(string_list[2:5])
# print(string_list[-1])
# print(new_string[-1])


# -----------------------------------------------------------------------------

# bracket_list = list((1,2,3 ))
# print(bracket_list)
# for element in digits_list.value():
    # print(element)