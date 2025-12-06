print("Sinh vien: LE HOANG VU")
print("Ma so SV : 245751030110084")
print("#############################")
n = int(input("Nhập n: "))

for i in range(n):
    row = [1] * (i+1)
    for j in range(1, i):
        row[j] = prev[j-1] + prev[j]
    print(row)
    prev = row

