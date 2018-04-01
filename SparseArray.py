class SparseArray:

    # -------------------------- nested Node class --------------------------
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

        def __str__(self):
            return str(self._element)  # Inside your node class

        #------------------------------- sparse array methods -------------------------------

    def __init__(self, size):
        self._data = [None] * size
        self._head = None
        self._size = size
        self._usage = 0

    def __len__(self):
        return self._size

    def __getitem__(self, item):
        return self._data[item]

    def __setitem__(self, key, value):
        """Add element e to the top of the stack."""
        newest = self._Node(value, self._head)  # create and link a new node
        self._data[key] = newest
        self._head = newest
        self._usage += 1

    def get_usage(self):
        return self._usage

    def fill(self, sequence):
        pass



