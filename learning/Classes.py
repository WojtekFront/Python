class Classes:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def __str__(self):
        return f'width: {self.width}, height: {self.height}'
    
    def __repr__(self):
        return f'width: {self.width}, height: {self.height}'
    
new_classes = Classes(25, 3)

print(repr(new_classes))


# print(new_classes.__str__())