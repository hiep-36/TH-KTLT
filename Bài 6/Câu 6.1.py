print("Le Hoa Hiep")
print("235752021610073")
import math
class Circle(object):
    def __init__(self, r):
        self.radius = r
    def area(self):
        return math.pi * self.radius ** 2
aCircle = Circle(2)
print(aCircle.area())
