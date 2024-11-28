def linear_search(arr, target):
  for i in range(len(arr)):
    if arr[i] == target:
      return i
  return -1

# Тест 1
assert linear_search([5, 3, 7, 1, 4], 1) == 3
# Тест 2
assert linear_search([10, 20, 30, 40], 30) == 2
# Тест 3
assert linear_search([1, 2, 3, 4], 5) == -1
# Тест 4
assert linear_search([1], 1) == 0
# Тест 5
assert linear_search([], 1) == -1
print("OK!")