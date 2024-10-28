g={}
for i in ([[i[0]+i[1],i[3]+i[4]] for i in open("iban_lenght.txt")]): g[i[1]]=i[0]
print(g)
