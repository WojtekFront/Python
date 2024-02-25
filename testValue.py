import random
# import docx

feet_in_miles = 5280
meter_in_kilometers = 1000
names = ["Mark", "Leon", "Gem", "Pair"]

def get_file_ext(filename) :
    return filename[filename.index(".")+1:]

def roll_dice(num):
    return random.randint(1, num)


# print(get_file_ext("employees.txt"))


# docx.HeaderPart("Employees")