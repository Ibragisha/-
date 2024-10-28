r = int(input())
print("Диаметр ", r*2)

s = 0
for i in range(100, 501):
    s += i
print(s)

s = 0
print("Введите число меньше 500")
a = int(input())
if a < 500:
    for i in range(a, 501):
        s += i
    print(s)