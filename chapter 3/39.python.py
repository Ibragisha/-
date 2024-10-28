import random

def f(n):
    if len(n) <= 3:
        return n
    q = list(n[1:-1])
    random.shuffle(q)
    return n[0] + ''.join(q) + n[-1]

def g(m):
    n = m.split()
    s = []
    for word in n:
        if word.isalpha():
            s.append(f(word))
        else:
            s.append(word)
    return ' '.join(s)
m = "Four score and seven years ago our fathers brought forth on this continent a new nation, conceived in liberty, and dedicated to the proposition that all men are created equal."
print(g(m))