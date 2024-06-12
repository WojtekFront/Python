
list1 = [0,1,2,3,4,5,5,6,6,7,7,8,8,9,9]
list2 = range(100)
list3 = [4,5,6,7,8,9,10]
list4 = [7,8,92,10,11,12,13,14]

import sys
new_values = 0
for x in list4:
    print("x={0}".format(x))
    print("new_values={0}".format(new_values))
    if not x:
        print("error)")
        sys.exit()
    elif new_values < x:
        new_values = x
print(new_values)     
    

# newest_list = list(map(lambda x,y: x+y, list1, list3))

# newest_list = [x+y for x,y in zip(list1, list3)]

# newest_list= list(filter(lambda x: x%2==0, map(lambda x, y: x+y, list1, list3)))

# newest_list = [x+y for x,y in zip(list1, list3)]
# print(newest_list)


# def sq(x):
#     return x**2

# result = map(sq, list1)

# for x in result:
#     print(x)




# filter_list = list(filter(lambda x: x%2==1, list4))
# print(filter_list)
# filter_list2 = [x for x in list4 if x%2 ==1]
# filter_list2 = [x*5 for x in list4 if x%2 ==1]
# print(filter_list2)

# new_list = list(map(sq, list3))
# print(new_list)
# zip_list = list(zip(list3, list4))
# print(zip_list)

# new_list = list(zip(list1,list2,list3))