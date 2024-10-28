gold_prices_1 = [100, 120, 140, 160, 180, 200, 220]
gold_prices_2 = [200, 180, 220, 160, 240, 260, 210]
gold_prices_3 = [250, 230, 210, 190, 170, 150, 130]
gold_prices_4 = [200, 200, 200, 200, 200, 200, 200]
gold_prices_5 = [150, 160, 155, 170, 180, 175, 165]

def f(i):
    if i.index(min(i))<i.index(max(i)):
        s=(max(i)-min(i))
    else:
        s=0
    return (i.index(max(i))+1,i.index(min(i))+1,s)
print(f(gold_prices_1))

print(f(gold_prices_2))
print(f(gold_prices_3))
print(f(gold_prices_4))
print(f(gold_prices_5))