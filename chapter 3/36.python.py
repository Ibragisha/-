def f(a):
    if not a:
        return []
    b = min(a)
    c = max(a)
    if b == c:
        return [0.0] * len(a)
    d = [(x - b) / (c - b) for x in a]
    return d
a = [2, 4, 10, 6, 8, 4]
print(f(a))