def ternary_search(arr, target):
  left, right = 0, len(arr) - 1
    
  while left <= right:
    mid1 = left + (right - left) // 3
    mid2 = right - (right - left) // 3
        
    if arr[mid1] == target:
      return mid1
    if arr[mid2] == target:
      return mid2
        
    if target < arr[mid1]:
      right = mid1 - 1
    elif target > arr[mid2]:
      left = mid2 + 1
    else:
      left = mid1 + 1
      right = mid2 - 1
    
  return -1

# Пример использования
sorted_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
index_of_five = ternary_search(sorted_numbers, 5)
print(index_of_five)  

index_of_ten = ternary_search(sorted_numbers, 10)
print(index_of_ten)  
# Тест 1
assert ternary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 5) == 4
# Тест 2
assert ternary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 3) == 2
# Тест 3
assert ternary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 1) == 0
# Тест 4
assert ternary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 10) == -1
# Тест 5
assert ternary_search([], 1) == -1  
print("Все тесты пройдены!")