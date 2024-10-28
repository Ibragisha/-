def f(x, y, a):
    r = ord(x[0].upper()) - ord('A')
    c = int(x[1:]) - 1
    if y == 'horizontal':
        if c + len(a) > 15:
            return False
    elif y == 'vertical':
        if r + len(a) > 15:
            return False
    else:
        return False
    
    return True

x = 'G7'
y = 'horizontal'
a = 'PRIVET'

if f(x, y, a):
    print(f"Слово '{a}' умещается на поле в позиции '{x}' по направлению '{y}'.")
else:
    print(f"Слово '{a}' не умещается на поле в позиции '{x}' по направлению '{y}'.")