print("Sinh vien: LE HOANG VU")
print("Ma so SV : 245751030110084")
print("#############################")
s = input("Nhập chuỗi: ")
kq = ""

for ch in s:
    if not ch.isdigit():   # nếu KHÔNG phải là số
        kq += ch

print(kq)

