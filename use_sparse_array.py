from SparseArray import SparseArray

# match assignment specifications
array = SparseArray(1000000)
print(len(array))
print(array.get_usage())
array[999999] = 42
print(array[999999])
print(array[-1])
print(array.get_usage())
print(array[0])
print(array[0] is None)

# will throw Index Error !
# print(array[1000000])

print("----------------------------------------------------")

# test Sparse Array fill method
array = [1,2,3,4,5,6,7,8]
S = SparseArray(10)
S[5] = "hello"
S[7] = "hello"
# display original array
for item in S:
    print(item)
print("----------------------------------------------------")

S.fill(array)
# display array with changes
for item in S:
    print(item)
print("----------------------------------------------------")

# display array item types

for item in S:
    print(type(item))
