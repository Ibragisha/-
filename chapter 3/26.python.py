pi=2.0
for i in range(1, 100000):
    pi *= ((4.0*i**2.0)/(4.0*i**2.0-1.0))
print(pi)