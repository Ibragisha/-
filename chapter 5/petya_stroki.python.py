def a(b, c):
    d = b.lower()
    e = c.lower()
    
    if d < e:
        return -1
    elif d > e:
        return 1
    else:
        return 0

f = "aaaa"
g = "aaaA"
h = a(f, g)
print(h)