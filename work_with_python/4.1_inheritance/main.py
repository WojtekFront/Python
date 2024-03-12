import csv
from items import Item


class Phone(Item):
    def __init__(self,name:str, model:str, color, price=1, quantity=1, *args):
        super().__init__(name, price, quantity, *args)
        self.pay_rate = 0.8 # pay rate for each item with a price of 0.8
        # self.all.append(self)
        self.model = model
        self.color = color

itemXXX = Item("phone",120,2)
phonexxx= Phone("Xiaomi", "X2", "black",4500, 1)

try:
    print(Item.all)
    print("--------------------------------")
    print(Phone.all)
except:
    print("error")