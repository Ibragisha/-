def tetr(tet,chis):
    s=1
    for i in range(tet):
        s=chis**s
    return len(str(s))
print(tetr(3,5))
print(tetr(5,2))