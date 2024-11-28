def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
    return arr

# Пример использования
numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = bubble_sort(numbers)
print(sorted_numbers)  # Ожидаемый вывод: [1, 2, 5, 5, 6, 9]
# Тест 1
assert bubble_sort([5, 2, 9, 1, 5, 6]) == [1, 2, 5, 5, 6, 9]
# Тест 2
assert bubble_sort([10, 7, 8, 9]) == [7, 8, 9, 10]
# Тест 3
assert bubble_sort([1]) == [1]
# Тест 4
assert bubble_sort([3, 3, 3, 2, 2]) == [2, 2, 3, 3, 3]
# Тест 5
assert bubble_sort([]) == []
print("OK!")