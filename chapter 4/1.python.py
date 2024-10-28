def f1(a,b):
    return a[0]*b[0]+a[1]*b[1]+a[2]*b[2]
def f2 (a,b):
    i=(a[1]*b[2]-a[2]*b[1])
    j = (a[0] * b[2] - a[2] * b[0])
    k = (a[0] * b[1] - a[1] * b[0])
    return [i,j,k]
def f3(a,b,c):
    a=[a[0]*b[0],a[1]*b[1],a[2]*b[2]]
    return a[0]*c[0]+a[1]*c[1]+a[2]*c[2]
def f4 (a,b):
    i=(a[1]*b[2]-a[2]*b[1])
    j = (a[0] * b[2] - a[2] * b[0])
    k = (a[0] * b[1] - a[1] * b[0])
    a=[i,j,k]
    i = (a[1] * b[2] - a[2] * b[1])
    j = (a[0] * b[2] - a[2] * b[0])
    k = (a[0] * b[1] - a[1] * b[0])
    return [i,j,k]