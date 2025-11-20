# Write a function that takes an array of numbers and returns the sum of the numbers. The numbers can be negative or non-integer. If the array does not contain any numbers then you should return 0.
# Examples
# Input: [1, 5.2, 4, 0, -1]
# Output: 9.2
# Input: []
# Output: 0
# Input: [-2.398]
# Output: -2.398

def sum_array(list):
    result = 0
    for emlement in list:
        result += emlement
    return result

def sum_array2(list):
    return sum(list)

# print(sum_array2([10,12,-12,-13.5]))
# print(sum_array2([0]))

