# -------------------------------------------



# def my_function(a, b):
#   return a + b 

# numbers = [1, 2]
# result = my_function(*numbers)
# print(result)



def my_function(title, *star, **kwargs):
  print("Title:", title)
  print("Positional arguments:", star)
  print("Keyword arguments:", kwargs["city"])
  print("Keyword arguments:", kwargs.get("age", "puste"))


# my_function("User Info", "Emil", "Tobias", "John",  city = "Oslo")



def nowafunkcja(**test):
    print("Name: " + test["name"])
    print("Lastname: " + test["lastname"])
    print("Lastname2: " + test.get("lastname2","Nieznane"))

# nowafunkcja(name="Jan", lastname ="Maria", lastname2 ="Rokita")
# nowafunkcja(name="Anna", lastname="Kowalska")



# nowafunkcja("Jan")


  



def nowafunkcja(*args):
    total =0
    for num in args:
        total +=num
    return total

# print(nowafunkcja(1,2,3,4))



# -------------------------------------------

def dictionaryArgument(person):
    print("Person age: " , person["age"])
    return 1

# person1 = { "name": "Emil", "age": 30}
# dictionaryArgument(person1)

# -------------------------------------------

# def dodawanie(x=10, y=1000):
#     return x + y

# print(dodawanie(1))
# print(dodawanie(y=1))

# -------------------------------------------

# furniture = ["kanapa Abra Kadabra"," stół End", "krzesło Rabarbar", "kanapa Eli"]
# krzesło = stół = inne = 0
# for article in furniture:
#     furnitureWords = article.lower().split()
    
#     # print(furnitureWords[0])
#     match furnitureWords[0]:
#         case "stół":
#             stół +=1
#         case "krzesło":
#             krzesło += 1
#         case _:
#             inne += 1

# print("krzesła: {0} szt., stół: {1} szt., inne: {2}".format(krzesło, stół, inne))

# -------------------------------------------

# b = list(a[:-1].upper())
# print(b)
# print(''.join(b))

# print(a[0:3])

# print("ra"not  in a)

# for i in range(len(a)):
#     print(a[2])

# import random
# a = float(1)
# a = float(str(1))
# # b = random.randrange(a,5)
# b =crandom.uniform(a, 7)
# print(b)

# day = 4 + 5j
# match day:
#     case 3:
#         print("eeee")
#     case _:
#         # day = str(day)
#         print(type(day))