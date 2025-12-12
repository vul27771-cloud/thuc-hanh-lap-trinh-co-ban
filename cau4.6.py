print("Sinh vien: LE HOANG VU")
print("Ma so SV : 245751030110084")
print("############################")
###################################

class StringHandler:
    def __init__(self):
        self.text = ""

    def get_String(self):
        self.text = input("Nhập một chuỗi: ")
    def print_String(self):
        print(self.text.upper())

obj = StringHandler()
obj.get_String()      
obj.print_String()    

