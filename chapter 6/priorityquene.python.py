class PriorityQueue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return len(self.elements) == 0

    def push(self, item, priority):
        self.elements.append((priority, item))
        self.elements.sort(key=lambda x: x[0])

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from an empty priority queue")
        return self.elements.pop(0)[1]

    def peek(self):
        if self.is_empty():
            return None
        return self.elements[0][1]

    def size(self):
        return len(self.elements)

# Пример использования
pq = PriorityQueue()

# Добавление элементов с приоритетом
pq.push("Задача 1", priority=2)
pq.push("Задача 2", priority=5)
pq.push("Задача 3", priority=1)

# Получение элемента с наивысшим приоритетом без удаления
print("Первый элемент с наивысшим приоритетом:", pq.peek())  # Ожидаемый вывод: Задача 3

# Извлечение элементов с наивысшим приоритетом по очереди
while not pq.is_empty():
    print("Обработка:", pq.pop())