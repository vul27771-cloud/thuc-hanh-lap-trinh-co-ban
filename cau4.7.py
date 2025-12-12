print("Sinh vien: LE TRONG TRUNG")
print("Ma so SV : 245751030110070")
print("############################")
###################################

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * (self.radius ** 2)
    def circumference(self):
        return 2 * math.pi * self.radius

c = Circle(5)
print("Diện tích hình tròn:", c.area())
print("Chu vi hình tròn:", c.circumference())
