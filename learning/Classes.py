class Classes:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
new_classes = Classes(25, 3)

print(new_classes.area())