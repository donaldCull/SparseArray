from SparseArray import SparseArray

array = SparseArray(1000000)
print(len(array))
print(array.get_usage())
array[999999] = 42
print(array[999999])
print(array[-1])
print(array.get_usage())
print(array[0])
print(array[0] is None)
print(array[1000000])

