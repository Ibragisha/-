def hamming_distance(s1, s2):
    if len(s1) != len(s2):
        raise ValueError("строки не равны")
    distance = sum(c1 != c2 for c1, c2 in zip(s1, s2))
    return distance
s1 = "karolin"
s2 = "kathrin"
print(f"Расстояние Хэмминга между '{s1}' и '{s2}' равно: {hamming_distance(s1, s2)}")