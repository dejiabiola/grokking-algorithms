def find_smallest(arr):
  # Assume the initial index is the smallest
  smallest = arr[0]
  smallest_index = 0

  # loop through all indexes and if there's any value smaller than the initial index, assign that value to be the smallest
  for i in range(1, len(arr)):
    if arr[i] < smallest:
      smallest = arr[i]
      smallest_index = i

  return smallest_index


def selection_sort(arr):
  new_arr = []
  for i in range(len(arr)):
    smallest = find_smallest(arr)
    new_arr.append(arr.pop(smallest))
  return new_arr

