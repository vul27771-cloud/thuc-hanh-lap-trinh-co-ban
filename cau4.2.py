print("Sinh vien: LE TRONG TRUNG")
print("Ma so SV : 245751030110070")
print("############################")
###################################

class Hinhchunhat:
    def __init__(self, chieu_dai, chieu_rong):
        # Khởi tạo đối tượng với chiều dài và chiều rộng
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong

    def dien_tich(self):
        # Phương thức tính diện tích hình chữ nhật
        return self.chieu_dai * self.chieu_rong


# Ví dụ sử dụng
hcn = Hinhchunhat(5, 3)
print("Diện tích hình chữ nhật là:", hcn.dien_tich())
