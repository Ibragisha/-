import math

class SparseTable:
    def __init__(self, array):
        self.n = len(array)  # Длина входного массива
        self.log = math.floor(math.log2(self.n)) + 1  # Максимальная степень двойки
        self.st = [[0] * self.log for _ in range(self.n)]  # Инициализируем таблицу
        self.build(array)

    def build(self, array):
        for i in range(self.n):
            self.st[i][0] = array[i]
        j = 1
        while (1 << j) <= self.n:
            i = 0
            while (i + (1 << j) - 1) < self.n:
                self.st[i][j] = min(self.st[i][j - 1], self.st[i + (1 << (j - 1))][j - 1])
                i += 1
            j += 1

    def query(self, left, right):
        length = right - left + 1
        j = math.floor(math.log2(length))  # Находим максимальную степень двойки, которая помещается в диапазон
        return min(self.st[left][j], self.st[right - (1 << j) + 1][j])

# Пример использования
array = [1, 3, 2, 7, 9, 11]
sparse_table = SparseTable(array)

# Запросы на нахождение минимума
print(sparse_table.query(1, 4))  # Ожидаемый вывод: 2
print(sparse_table.query(0, 5))  # Ожидаемый вывод: 1
print(sparse_table.query(2, 2))  # Ожидаемый вывод: 2