from decimal import Decimal, ROUND_HALF_UP

class Item:
    def __init__(self,name, price, quantity, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        print(f"An instance created: {name}")
    def calculate_total_price(self, price, amount):
        return (price * amount).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

item1 = Item("Motorlla", 200.54, 20)
item1.name = "Phone"
item1.price = Decimal(100.04)
item1.quantity = int(10)
print(item1.calculate_total_price(item1.price, item1.quantity))


# item2 = Item()
# item2.name = "Laptop"
# item2.price = Decimal(1200.04)
# item2.quantity = int(2)



