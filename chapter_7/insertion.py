def insertion_sort(arr):
  for i in range(1, len(arr)):
      key = arr[i]
      j = i - 1
      while j >= 0 and key < arr[j]:
          arr[j + 1] = arr[j]
          j -= 1
      arr[j + 1] = key
  return arr

# Пример использования
grades = [5, 2, 9, 1, 5, 6]
sorted_grades = insertion_sort(grades)
print(sorted_grades)  
# Тест 1
assert insertion_sort([5, 2, 9, 1, 5, 6]) == [1, 2, 5, 5, 6, 9]
# Тест 2
assert insertion_sort([10, 7, 8, 9]) == [7, 8, 9, 10]
# Тест 3
assert insertion_sort([1]) == [1]
# Тест 4
assert insertion_sort([3, 3, 3, 2, 2]) == [2, 2, 3, 3, 3]
# Тест 5
assert insertion_sort([]) == []
print("OK!")