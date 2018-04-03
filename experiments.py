from SparseArray import SparseArray
from time import time
from random import randrange


def manual_set_get_sparse_array(n, m):
    """
    Manually set and get random items from sparse array

    :param n: size of SparseArray
    :param m: Memory utilised in Sparse Array
    :return: Average run-time of random get and set actions
    """
    time_start = time()
    s_array = SparseArray(n)
    times_accessed = 0
    for index in range(m):
        rand_index = randrange(n)
        times_accessed += 1
        # set random position in SparseArray to random value
        s_array[rand_index] = rand_index
        # Access random position in SparseArray
        rand_item = s_array[rand_index // 2]

    time_end = time()
    return (time_end - time_start) / times_accessed

def fill_sparse_experiment(n, m):
    """
    Measure run-time of fill method with different sizes of n and m

    :param n: size of SparseArray
    :param m: Memory utilised in Sparse Array
    :return: run-time of fill method
    """
    s_array = SparseArray(n)
    array = ["blah"] * m
    time_start = time()
    s_array.fill(array)
    time_end = time()
    return time_end - time_start

def set_element_sparse(n):
    """
    Measure a set operation in a random position within sparse array of n size

    :param n: size of Sparse Array
    :return: time of random set operation in SparseArray
    """
    s_array = SparseArray(n)
    rand_index = randrange(n)
    time_start = time()
    s_array[rand_index] = rand_index
    time_end = time()
    return time_end - time_start

def get_element_sparse(n):
    """
    Measure a get operation in a random position within sparse array of n size

    :param n: size of Sparse Array
    :return: time of random get operation in SparseArray
    """
    s_array = SparseArray(n)
    rand_index = randrange(n)
    time_start = time()
    rand_item = s_array[rand_index]
    time_end = time()
    return time_end - time_start


print("----------------------------------------------------")

# Unable to create a SparseArray bigger than 10^8
for i in range(3, 9):
    print("Sparse Array Average of {0:.3f} with n = 10^{1} and m = 5^{2}".format(manual_set_get_sparse_array(10 ** i, 5 ** i) * 1000000, i, i))

print("----------------------------------------------------")

for i in range(3, 9):
    print("Sparse fill of {0:.3f} with n = 10^{1} and m = 5^{2}".format(fill_sparse_experiment(10 ** i, 5 ** i) * 1000000, i, i))

print("----------------------------------------------------")

for i in range(3, 9):
    print("Sparse set time of {0:.3f} with n = 10^{1}".format(set_element_sparse(10 ** i) * 1000000, i, i))
print("----------------------------------------------------")

for i in range(3, 9):
    print("Sparse get time of {0:.3f} with n = 10^{1}".format(get_element_sparse(10 ** i) * 1000000, i, i))
