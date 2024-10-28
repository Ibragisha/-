for i in range(1,4141241):
    s=1
    s1=0
    for i1 in range(1,i):
       s*=i1
    for i1 in str(s):
        s1+=int(i1)
    if s%s1!=0:
        print(i)
        break