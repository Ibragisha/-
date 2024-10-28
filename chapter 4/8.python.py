def f(k):
    k1=k+1
    for i in range(1,2414141241):
        x=k*i
        x1=k1*i
        s=0
        for i1 in '0123456789':
            if str(x1).count(i1)==str(x).count(i1):
                s+=1
        if s==10:
            return i

print(f(325),"  ",f(100))