def min_max(nums):
  if nums:
    return (min(nums), max(nums))
  else:
    return ValueError

def unique_sorted(nums):
  return sorted(set(nums))

def flatten(mat):
  arr = []
  for x in mat:
    if not isinstance(x, list) and not isinstance(x, tuple):
      return TypeError
    arr.extend(x)
  return arr

arr1 = [[3, -1, 5, 5, 0], [42], [-5, -2, -9], [], [1.5, 2, 2.0, -3.1]]
print('min_max:')
for x in arr1:
  print(f'{x} -> {min_max(x)}')
arr2 = [[3, 1, 2, 1, 3], [], [-1, -1, 0, 2, 2], [1.0, 1, 2.5, 2.5, 0]]
print('unique_sorted:')
for x in arr2:
  print(f'{x} -> {unique_sorted(x)}')
arr3 = [[[1, 2], [3, 4]], ([1, 2], (3, 4, 5)), [[1], [], [2, 3]], [[1, 2], "ab"]]
print('flatten:')
for x in arr3:
  print(f'{x} -> {flatten(x)}')