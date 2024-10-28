def race(x,y,g):
    if x>=y:
        return [-1,-1,-1]
    t1=int((g/(y-x)))
    g-=(y-x)*t1
    t2=int((g/(y-x))*60)
    g -= ((y - x) * t2/60)
    t3=int((g / (y - x)*3600))
    return t1,t2,t3
print(race(720, 850, 70))
print(race(80,91,37))