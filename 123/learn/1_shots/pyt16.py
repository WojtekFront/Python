# -------------------------------------------
# -------------------------------------------

def dictionaryArgument(person):
    print("Person age: " , person["age"])
    return 1

person1 = { "name": "Emil", "age": 30}
dictionaryArgument(person1)








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