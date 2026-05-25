class Point:
    def __init__ (self, x, y):
        self.x = x 
        self.y = y
    
    def falls_within_rectangle(self, lowerleft, upperright):
        if lowerleft[0] <= self.x <= upperright[0] \
            and lowerleft[1] <= self.y <= upperright[1]:
            return True
        else:         return False

class Rectangle:
    def __init__ (self, lowerleft, upperright):
        self.lowerleft = lowerleft
        self.upperright = upperright
    
pointx = Point(11,7)

rec = Rectangle((5,5), (10,10))

print(pointx.falls_within_rectangle(rec.lowerleft, rec.upperright))

