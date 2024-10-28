m = []

for a in range(10):
    m.append(a)

number = int(input())
for part in m:
    print(str(number) + " * " + str(part) + " = " + str(number * part))