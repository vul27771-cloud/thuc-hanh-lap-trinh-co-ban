print("Sinh vien: LE TRONG TRUNG")
print("Ma so SV : 245751030110070")
print("############################")
###################################

class Circle:
    def __init__(self, r):
        # Khởi tạo đối tượng với bán kính r
        self.radius = r

    def area(self):
        # Phương thức tính diện tích hình tròn
        return self.radius ** 2 * 3.14

aCircle = Circle(2)
print("Diện tích hình tròn là:", aCircle.area())

