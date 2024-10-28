def b(x):
    return x * 1024

def kb(x):
    return x / 1024

a = int(input())
print("Из килобайт в байты:", bytes(a), ". Из байт в килобайты", kb(a))