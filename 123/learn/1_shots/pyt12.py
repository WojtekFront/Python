# Given an array of integers, return a new array with each value doubled.
# For example:
# [1, 2, 3] --> [2, 4, 6]


def maps(a):
    new_list=[]
    for x in a:
        new_list.append(x*2)
    return new_list




def maps2(a):
    return [2 * x for x in a]

def maps3(a):
    blabla = [3* x for x in a]
    return blabla
print(maps3([1,2,3]))