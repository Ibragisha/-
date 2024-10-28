import random
import time

def a(b):
    if len(b) <= 1: return b
    c = len(b) // 2
    d = a(b[:c])
    e = a(b[c:])
    return f(d, e)

def f(d, e):
    g = []
    h = i = 0
    while h < len(d) and i < len(e):
        if d[h] < e[i]:
            g.append(d[h])
            h += 1
        else:
            g.append(e[i])
            i += 1
    g.extend(d[h:])
    g.extend(e[i:])
    return g

def j(b):
    for k in range(len(b)):
        l = k
        for m in range(k + 1, len(b)):
            if b[m] < b[l]: l = m
        b[k], b[l] = b[l], b[k]
    return b

def n(o):
    return [random.randint(1, 1000) for _ in range(o)]

def p():
    for q in [100, 1000, 10000, 100000]:
        r = n(q)
        s = time.time()
        a(r.copy())
        t = time.time() - s
        s = time.time()
        j(r.copy())
        u = time.time() - s
        print(f"Размер списка: {q}")
        print(f"Время выполнения сортировки слиянием: {t:.5f} сек")
        print(f"Время выполнения сортировки выбором: {u:.5f} сек")
        print("="*50)

if __name__ == "__main__":
    p()