def binary_gcd(x, y):
    if x==0 and y==0:
        return 0
    if x==0:
        x=y
    if y==0:
        y=x
    if x<0:
        x*=-1
    if y<0:
        y*=-1
    if x>0:s=sorted([i for i in range(1, int(x ** 0.5) + 1) if x % i == 0 for i in (i, x // i)])
    if y > 0:s1 = sorted([i for i in range(1, int(y ** 0.5) + 1) if y % i == 0 for i in (i, y // i)])
    s=s[::-1]
    s1 = s1[::-1]
    g=[]
    for i in s:
        for i1 in s1:
            if i==i1:
                g.append(i)
    return (str(bin(max(g))[2::]).count("1"))
print(binary_gcd(666666, 333111))
print(binary_gcd(545034,5))
print(binary_gcd(0, 0))
print(binary_gcd(0, 76899299))
print(binary_gcd(666666, 333111))
print(binary_gcd(-124, -16))