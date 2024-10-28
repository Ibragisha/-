a=[1,2,3]
b=1
c=[]
for i in a:
    b*=i
for i in a:
    c.append(b//i)
print(c)