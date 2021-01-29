import list_util

assert list_util.equals(list_util.filter_by_list([0, 1, 2, 3], [5, 6, 3, 4]), [0, 1, 2]) == True


assert list_util.equals(list_util.filter_zeros([1, 0, 24, 0, 0, 5]), [1, 24, 5]) == True
assert list_util.equals(list_util.filter_zeros([0, 0, 24, 0, 3, 5]), [24, 3, 5]) == True
assert list_util.equals(list_util.filter_zeros([0, 0, 0, 1, 0, 5]), [1, 5]) == True

print("OK")
