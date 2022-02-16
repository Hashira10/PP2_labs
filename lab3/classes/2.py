class Shape():
    def __init__(self):
        pass
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, len):
        Shape.__init__(self)
        self.length = len
    
    def area(self):
        return self.length**2
b = int(input())
a = Square(b)
print(a.area())