print("Sinh vien: LE HOANG VU")
print("Ma so SV : 245751030110084")
print("#############################")
total = 0

while True:
    s = input()
    if not s:
        break
    
    action, value = s.split()
    value = int(value)

    if action == 'D':
        total += value
    elif action == 'W':
        total -= value

print("Số dư cuối:", total)

