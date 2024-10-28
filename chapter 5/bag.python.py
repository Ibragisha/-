def f(a,b):
    s=[]
    for i in a:
        s.append([i[1]//i[0],i[0]])
    s.sort()
    s=s[::-1]
    sum=0
    for i,j in s:
        b-=j
        if b<0:
            b+=j
            continue
        else:
            sum+=i*j

    return sum,b
# 1. Вес предмета
# 2. Стоимость предмета

items_1 = [(2, 10), (3, 15), (5, 30)]
weight_limit_1 = 5

items_2 = [(2, 10), (3, 15), (5, 30), (7, 20), (1, 5), (4, 10)]
weight_limit_2 = 10

items_3 = [(2, 20), (3, 15), (5, 30), (1, 25), (4, 10)]
weight_limit_3 = 7

items_4 = [(2, 5), (3, 8), (5, 15), (1, 3), (4, 10)]
weight_limit_4 = 7

items_5 = [(6, 10), (8, 15), (12, 30)]
weight_limit_5 = 5
print(f(items_1,weight_limit_1))
print(f(items_2,weight_limit_2))
print(f(items_3,weight_limit_3))
print(f(items_4,weight_limit_4))
print(f(items_5,weight_limit_5))