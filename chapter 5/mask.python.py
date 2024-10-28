def f(a,b,c):
    h=[]
    for i in a:
        s=[]
        s1=i[0]
        s2=i[1]
        s3=i[2]
        s.append([(i[0]/i[1]),(i[0]/i[2]),i[1],i[2]])
        for i in s:
            if i[2]>i[3]:
                h.append([(i[0]/i[1]),s1,s2,s3])
            else:
                h.append([(i[1] / i[0]),s1,s2,s3])
    h.sort()
    h = h[::-1]
    sum = 0
    for i1,i2,i3,i4 in h:
        b -= i3
        c-= i4
        if b < 0 :
            b += i3
            c+=i4
            continue
        if c < 0 :
            c += i4
            b+=i3
            continue
        else:
            sum += i2

    return sum

items_1 = [(10, 5, 2), (15, 4, 3), (30, 7, 5)]
time_limit_1 = 10
weight_limit_1 = 10
items_2 = [(20, 6, 4), (15, 3, 3), (25, 5, 5), (10, 2, 2), (12, 4, 3)]
time_limit_2 = 12
weight_limit_2 = 10

items_3 = [(15, 5, 3), (12, 4, 2), (30, 7, 5), (25, 6, 4), (20, 3, 3)]
time_limit_3 = 15
weight_limit_3 = 12

items_4 = [(10, 4, 2), (20, 5, 3), (15, 3, 2), (25, 6, 4), (18, 4, 3)]
time_limit_4 = 13
weight_limit_4 = 11

items_4 = [(10, 4, 2), (20, 5, 3), (15, 3, 2), (25, 6, 4), (18, 4, 3)]
time_limit_4 = 13
weight_limit_4 = 11
print(f(items_1,time_limit_1,weight_limit_1))
print(f(items_2,time_limit_2,weight_limit_2))
print(f(items_3,time_limit_3,weight_limit_3))
print(f(items_4,time_limit_4,weight_limit_4))