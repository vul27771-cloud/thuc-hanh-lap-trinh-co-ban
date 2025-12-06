print("Sinh vien: LE HOANG VU")
print("Ma so SV : 245751030110084")
print("#############################")
ds = input("Nhập dãy từ: ").split()

maxlen = max(len(t) for t in ds)

for t in ds:
    if len(t) == maxlen:
        print(t)

