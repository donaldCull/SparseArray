from SparseArray import SparseArray

# array = SparseArray(1000000)
# print(len(array))
# print(array.get_usage())
# array[999999] = 42
# print(array[999999])
# print(array[-1])
# print(array.get_usage())
# print(array[0])
# print(array[0] is None)
# print(array[1000000])

array = [1,2,3,4,5,6,7,8]
S = SparseArray(10)
S[5] = "hello"
S[7] = "hello"
for item in S:
    print(item)
print()
S.fill(array)
for item in S:
    print(item)
