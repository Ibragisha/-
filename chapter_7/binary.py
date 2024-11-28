def binary_search(arr, target):
  left, right = 0, len(arr) - 1
    
  while left <= right:
    mid = (left + right) // 2
    if arr[mid] == target:
      return mid
    elif arr[mid] < target:
      left = mid + 1
    else:
      right = mid - 1
    
  return -1


# Пример использования
sorted_numbers = [1, 2, 3, 4, 5, 6, 7]
index_of_four = binary_search(sorted_numbers, 4)
print(index_of_four) 

index_of_eight = binary_search(sorted_numbers, 8)
print(index_of_eight)  
# Тест 1
assert binary_search([1, 2, 3, 4, 5, 6, 7], 4) == 3
# Тест 2
assert binary_search([1, 2, 3, 4, 5, 6, 7], 6) == 5
# Тест 3
assert binary_search([1, 2, 3, 4, 5, 6, 7], 1) == 0
# Тест 4
assert binary_search([1, 2, 3, 4, 5, 6, 7], 8) == -1
# Тест 5
assert binary_search([], 1) == -1  
print("Все тесты пройдены!")