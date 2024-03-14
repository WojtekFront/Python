

class Person:
    language = "Polish"
    age = 25

wojtek = Person()
setattr(wojtek, "work", "self")

print(wojtek.work)