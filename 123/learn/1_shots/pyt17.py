def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

print(myfunction())


# ----
x = 300
def myfunc(x):
    def myinnerfunc(x):
        return x
        # print(x)
    myinnerfunc(x)
myfunc(x)