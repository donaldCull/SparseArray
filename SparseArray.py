class SparseArray:

    # -------------------------- nested Node class --------------------------
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

#------------------------------- sparse array methods -------------------------------

    def __init__(self, size):
        self._data = [None] * size
        self._head = None
        self._size = size

    def __len__(self):
        return self._size

    def __getitem__(self, item):
        pass

    def __setitem__(self, key, value):

        pass

    def get_usage(self):
        pass

    def fill(self, sequence):
        pass



