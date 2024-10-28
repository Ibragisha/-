a=[0,1]
print (0)
print(1)

for i in range(0,10000):
    a.append(a[i]+a[i+1])
    print(a[i]+a[i+1])
print(a[-1])
