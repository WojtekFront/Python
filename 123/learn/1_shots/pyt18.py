#  --------------------------
#  --------------------------
def dodaj_prefix(prefix):
    def decoratr(func):
        def wrapper():
            return prefix + " " + func()
        return wrapper
    



#  --------------------------
def changecase(func):
    def innerFunc(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return innerFunc



#  --------------------------
def updateCase(func):
    def myinner():
        return func().upper()
    return myinner
def lowerCase(func):
    def myinner():
        return func().lower()
    return myinner

@lowerCase
@updateCase
def test():
    return "Hello"

# print(test())