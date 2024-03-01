class Classes:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        print("long text width")
        return self._width
    
    @property
    def height(self):
        print("long text height")
        return self._height
    
    # def get_width(self):
    #     return self._width

    # def set_width(self, width):
    #     if width <= 0:
    #         raise ValueError('Width must be positive')
    #     else: 
    #         self._width = width

    def area(self):
        return self._width * self._height
    
    def __str__(self):
        return f'width: {self._width}, height: {self._height}'
    
    def __repr__(self):
        return f'width: {self._width}, height: {self._height}'
    
    def __eq__(self, other):
         if isinstance(other, Classes):
            return self._width == other._width and self._height == other._height
         else:
             return False
         
    def __lt__(self, other):
        if isinstance(other, Classes):
            return self.area() < other.area()
        else:
            return NotImplemented
    
new_classes = Classes(25, 3)
# new_classes.set_width(-100)
new_classes._width=10
print(new_classes.width)


# new_classes2 = Classes(25, 31)
# print(new_classes > new_classes2)
# print(new_classes.__str__())