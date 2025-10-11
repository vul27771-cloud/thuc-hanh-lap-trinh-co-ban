print("sinh vien : le hoang vu")
print("ma so sv :245751030110084")
print("#############################")
#bai1
n1=int(input("enter n1 value:"))
n2=int(input("enter n2 value:"))
if n1 > n2:
     print("n1 is big")
else:
     print("n2 is big")

#bai2
import math
x1 = float(input("enter x1 -->"))
y1 = float(input("enter y1 -->"))
x2 = float(input("enter x2 -->"))
y2 = float(input("enter y2 -->"))
dx = x2-x1
dy = y2-y1
dist= math.sqrt(dx*dx+dy*dy)
print("distance between two points:",dist)

 #bai3  
n =int(input("enter a number -->"))
if n%2==0:
     print("even number")
else:
     print("ODD number")


# Bài 4: in số và nghịch đao
a=int(input("enter a:"))
b=int(input("enter b:"))
for i in range (a+1,b):
     nghich_dao =1/i
     print("so:",i," -> ngich dao =", nghich_dao)
#bai 5
n=int(input(" enter A number--->"));
while n>=0:
     print (n)
     n = n-1
#bai 6

nums = []
for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        nums.append(str(i))

print(",".join(nums))
#bai7
n = int(input("Nhập vào một số nguyên n: "))
d = {}

for i in range(1, n + 1):
    d[i] = i * i

print(d)
#bai8

a, b = 1, 2
total = 0

print(a, b, end=" ")

while b < 4000000:
    if b % 2 == 0:
        total += b
    a, b = b, a + b
    print(b, end=" ")

print("\nTổng các số chẵn trong dãy Fibonacci:", total)
#bai9
s = input("Enter a string: ")
d = {}

for ch in s:
    if ch in d:
        d[ch] += 1
    else:
        d[ch] = 1

print(d)
#bai 10
a = "hi i am python programmer"
b = a.split()
print(b)   # ['hi', 'i', 'am', 'python', 'programmer']

c = " ".join(b)
print(c)   # "hi i am python programmer"
#bai11
l = [1, 'python', 4, 7]
k = ['cse', 2, 'guntur', 8]

m = []
m.append(l)
m.append(k)

print("Danh sách sau khi nối:", m)

d = {'l': l, 'k': k, 'combine_list': m}
print("Từ điển:", d)

