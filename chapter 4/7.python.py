def f(n,k):
    s=0
    for i in range(1,n+1):
        if k**i>n:
            break
        s+=n//k**i
    return s
print(f(10,2))