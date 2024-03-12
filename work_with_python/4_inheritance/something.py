from abc import ABC


class Something:
    def __init__(self, exists, weight):
        self.exists = exists
        self.weight = weight

    def print_waight(self)->int:
            print(self.weight)
        
stone = Something(True, 1)
# stone.print_waight()