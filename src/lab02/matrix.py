def transpose(mat):
  if len(mat) == 0: return []
  new_mat = [[] for x in mat[0]]
  for row in mat:
    if len(row) != len(new_mat):
      return ValueError
    for i, x in enumerate(row):
      new_mat[i].append(x)
  return new_mat

def row_sums(mat):
  for row in mat:
    if len(row) != len(mat[0]):
      return ValueError
  return [sum(row) for row in mat]

def col_sums(mat):
  if len(mat) == 0: return []
  new_mat = [0 for x in mat[0]]
  for row in mat:
    if len(row) != len(new_mat):
      return ValueError
    for i, x in enumerate(row):
      new_mat[i] += x
  return new_mat

arr1 = [[[1, 2, 3]], [[1], [2], [3]], [[1, 2], [3, 4]], [], [[1, 2], [3]]]
print('transpose:')
for x in arr1:
  print(f'{x} -> {transpose(x)}')
arr2 = [[[1, 2, 3], [4, 5, 6]], [[-1, 1], [10, -10]], [[0, 0], [0, 0]], [[1, 2], [3]]]
print('row_sums:')
for x in arr2:
  print(f'{x} -> {row_sums(x)}')
arr3 = [[[1, 2, 3], [4, 5, 6]], [[-1, 1], [10, -10]], [[0, 0], [0, 0]], [[1, 2], [3]]]
print('col_sums:')
for x in arr3:
  print(f'{x} -> {col_sums(x)}')