

class Person:
    language = "Polish"
    age = 25


# print(getattr(Person, 'language'))
# setattr(Person, "language","English")
# setattr(Person,"name", "Johny")
# print(Person.name)
# delattr(Person, "age")
# try:
#     print(getattr(Person, 'age'))
# except:
#     print("Attribute does not exist")
# print(Person.__dict__)