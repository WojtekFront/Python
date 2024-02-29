class Classes:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def to_string(self):
        return f'width: {self.width}, height: {self.height}'
    
new_classes = Classes(25, 3)

print(new_classes.t())