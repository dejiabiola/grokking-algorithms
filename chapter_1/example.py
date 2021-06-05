#! Simple example of binary search. Example of real life binary search is searching for a word in the dictionary or an address
# in the address book


def binary_search(list, item):
  low = 0
  high = len(list) - 1

  while low <= high:
    mid = int((low + high) / 2)
    guess = list[mid]
    if guess == item:
      return mid
    elif guess > item:
      high = mid - 1
    elif guess < item:
      low = mid + 1
  return None


my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 9))
