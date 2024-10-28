class Heap:
    def __init__(self, max_heap=True):
        self.heap = []
        self.max_heap = max_heap

    def is_empty(self):
        return len(self.heap) == 0

    def size(self):
        return len(self.heap)

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def extract(self):
        if self.is_empty():
            raise IndexError("Куча пуста")
        root_value = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._heapify_down(0)
        return root_value

    def peek(self):
        if self.is_empty():
            raise IndexError("Куча пуста")
        return self.heap[0]

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0:
            if (self.max_heap and self.heap[index] > self.heap[parent_index]) or \
               (not self.max_heap and self.heap[index] < self.heap[parent_index]):
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                self._heapify_up(parent_index)

    def _heapify_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        largest_or_smallest = index

        if left_child_index < len(self.heap):
            if (self.max_heap and self.heap[left_child_index] > self.heap[largest_or_smallest]) or \
               (not self.max_heap and self.heap[left_child_index] < self.heap[largest_or_smallest]):
                largest_or_smallest = left_child_index

        if right_child_index < len(self.heap):
            if (self.max_heap and self.heap[right_child_index] > self.heap[largest_or_smallest]) or \
               (not self.max_heap and self.heap[right_child_index] < self.heap[largest_or_smallest]):
                largest_or_smallest = right_child_index
        if largest_or_smallest != index:
            self.heap[index], self.heap[largest_or_smallest] = self.heap[largest_or_smallest], self.heap[index]
            self._heapify_down(largest_or_smallest)


# Пример использования
h = Heap(max_heap=True)  # Создаем максимальную кучу

# Вставка элементов
h.insert(10)
h.insert(4)
h.insert(15)
h.insert(20)
h.insert(3)

print("Корень кучи:", h.peek())  # Ожидаемый вывод: 20

# Извлечение корней
while not h.is_empty():
    print("Извлеченный элемент:", h.extract())