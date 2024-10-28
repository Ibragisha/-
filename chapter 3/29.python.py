a=input()
print((a.count("G")+a.count('C'))/(a.count('A')+a.count('A')+a.count('T')+a.count('C')+a.count('G')))
if (a==a[::-1]):
    print(a," - полиндром")
else:
    print(a," - не полиндром")