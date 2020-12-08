def comp(array1, array2):
    return None not in [array1, array2] and \
           sorted([abs(a) for a in array1]) == sorted([pow(abs(a), 0.5) for a in array2])


arr1 = [121, 144, 19, 161, 19, 144, 19, 11]
arr2 = [11 * 11, 121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144, 19 * 19]
print(comp(arr1, arr2), True)
arr1 = [4, 4]
arr2 = [1, 31]
print(comp(arr1, arr2), False)
arr1 = [121, 144, 19, 161, 19, 144, 19, 11]
arr2 = [11 * 21, 121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144, 19 * 19]
print(comp(arr1, arr2), False)
arr1 = [121, 144, 19, 161, 19, 144, 19, 11]
arr2 = [11 * 11, 121 * 121, 144 * 144, 190 * 190, 161 * 161, 19 * 19, 144 * 144, 19 * 19]
print(comp(arr1, arr2), False)
arr1 = []
arr2 = []
print(comp(arr1, arr2), True)
arr1 = []
arr2 = None
print(comp(arr1, arr2), False)
arr1 = [121, 144, 19, 161, 19, 144, 19, 11, 1008]
arr2 = [11 * 11, 121 * 121, 144 * 144, 190 * 190, 161 * 161, 19 * 19, 144 * 144, 19 * 19]
print(comp(arr1, arr2), False)
arr1 = [10000000, 100000000]
arr2 = [10000000 * 10000000, 100000000 * 100000000]
print(comp(arr1, arr2), True)
arr1 = [10000001, 100000000]
arr2 = [10000000 * 10000000, 100000000 * 100000000]
print(comp(arr1, arr2), False)
arr1 = [2, 2, 3]
arr2 = [4, 9, 9]
print(comp(arr1, arr2), False)
arr1 = [2, 2, 3]
arr2 = [4, 4, 9]
print(comp(arr1, arr2), True)
arr1 = None
arr2 = []
print(comp(arr1, arr2), False)
print(comp([], [1]), False)
arr1 = [-121, -144, 19, -161, 19, -144, 19, -11]
arr2 = [11 * 11, 121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144, 19 * 19]
print(comp(arr1, arr2), True)
