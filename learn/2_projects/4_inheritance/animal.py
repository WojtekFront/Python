from dataclasses import dataclass
from abc import ABC, abstractmethod
from something import Something

@dataclass
class Animal(Something):
    # pass
    def __init__(self, race, gender, age,exists, weight=1, name = "BOB", height= 1  ):
        super.__init__(self,exists, weight)
        self.race = race
        self.gender = gender
        self.age = age
        self.name = name
        self.height = height

try:
    dog = Animal("dog","male",5,True,5,"BOB", 1)
    dog = Animal .print_waight
except Exception e:
    print(e)