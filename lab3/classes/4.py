class Point():
    def __init__(self,x, y):
        self.x = x
        self.y = y
        self.old_x = 0
        self.old_y = 0
    def show(self):
        print("( " + str(self.x) + " ; " + str(self.y) + " )")

    def move(self,b,c):
        self.old_x = self.x 
        self.old_y = self.y 
        self.x = b 
        self.y = c
        
    def dist(self):
        return ((self.x - self.old_x)**2 + (self.y - self.old_y)**2)**0.5


a,b,c,d = map(int, input().split())
l = Point(a,b)
l.show()
l.move(c,d)
print(l.dist())
