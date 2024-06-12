try:
    new_int = int(input("please enter a number: "))
except ZeroDivisionError as err:
    print(err)
    exit()
except ValueError as err:
    print(err)
    exit()  

print(new_int)
