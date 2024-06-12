from decimal import Decimal, ROUND_HALF_UP

class Item:
    pay_rate = 0.8 # pay rate for each item with a price of 0.8
    all = []

    def __init__(self,name:str , price=1, quantity=1, *args):
        try: 
            self.name = name
            self.price = price
            self.quantity = quantity
        
        except ValueError as e:
            print("Error:  {0}   \n\n".format(e))
            exit(2)
        
    def calculate_total_price(self):
        return (self.price * self.quantity).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

    def apply_discount(self):
        price = (self.price * Item.pay_rate)#.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        return price
try:
    item1 = Item("Motorlla", 100, 20)
    item2 = Item("Computer", 1000, 2)
    item3 = Item("Mouse", 15, 10)
    item4 = Item("Keyboard", 30, 3)
    item5 = Item("Monitor", 1000, 10)

except Exception as e:
    print("incorrect value{0}".format(e))


# print(item1.apply_discount())
# print(Item.pay_rate)
# print(item1.calculate_total_price())






