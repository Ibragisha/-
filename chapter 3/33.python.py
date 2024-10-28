print("введите не четное число")
a=int(input())
s=1
if a%2!=0:
    for i in range (1,a):
        if i%2!=0:
            s*=i

    print("двойной фактариал равен=",s)
else:
    print("вы ввели четное число")
print("введите четное число")
a=int(input())
s=1
if a%2==0:
    for i in range (1,a):
        if i%2==0:
            s*=i
    print("двойной фактариал равен=",s)
else:
    print("вы ввели не четное число")