def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

    return arr
    
# Пример использования
numbers = [12, 34, 54, 2, 3]
sorted_numbers = shell_sort(numbers)
print(sorted_numbers)  
# Тест 1
assert shell_sort([12, 34, 54, 2, 3]) == [2, 3, 12, 34, 54]
# Тест 2
assert shell_sort([10, 7, 8, 9]) == [7, 8, 9, 10]
# Тест 3
assert shell_sort([1]) == [1]
# Тест 4
assert shell_sort([3, 3, 3, 2, 2]) == [2, 2, 3, 3, 3]
# Тест 5
assert shell_sort([]) == []
print("Все тесты пройдены!")