print("Sinh vien: LE HOANG VU")
print("Ma so SV : 245751030110084")
print("############################")
###################################


class Nguoi(object):
    def getGender(self):
        return "Unknown"

class Nam(Nguoi):
    def getGender(self):
        return "Nam"

class Nu(Nguoi):
    def getGender(self):
        return "Nữ"

aNam = Nam()
aNu = Nu()

print(aNam.getGender()) 
print(aNu.getGender())   





