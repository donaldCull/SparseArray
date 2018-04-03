class SparseArray:
    """
    Implementation of SparseArray utilising private Node subclass
    """

    # -------------------------- nested Node class --------------------------
    class _Node:
        """
        Private Node class used to fill sparse array
        """
        __slots__ = '_element', '_next'

        def __init__(self, element, reference):
            """

            :param element: value stored in Node
            :param reference: Pointer to next Node
            """
            self._element = element
            self._next = reference

        def __str__(self):
            """

            :return: String value of Node's value
            """
            return str(self._element)

            # ------------------------------- SparseArray methods -------------------------------

    def __init__(self, size):
        """
        Create new SparseArray
        :param size: size of the array
        """
        self._data = [None] * size
        self._head = None
        self._size = size
        self._usage = 0

    def __str__(self):
        """
        Allows printing of list
        :return: formatted string of values SparseArray
        """
        array = [str(item) for item in self._data]
        return "{}".format(array)

    def __len__(self):
        """

        :return: size of the array
        """
        return self._size

    def __iter__(self):
        """

        :return: Allow iteration of SparseArray
        """
        return iter(self._data)

    def __getitem__(self, item):
        """

        :param item: item index
        :return: item at requested index
        """
        return self._data[item]

    def __setitem__(self, key, value):
        """
        Create Node at selected position with value

        :param key: index position of new value
        :param value: value of new item
        :return: None
        """
        newest = self._Node(value, self._head)  # create and link a new node
        self._data[key] = newest
        self._head = newest
        self._usage += 1

    def get_usage(self):
        """

        :return: Number of positions allocated to Nodes
        """
        return self._usage

    def fill(self, array):
        """
        Fill SparseArray with new array values
        :param array: Array of values to fill
        :return: None
        """
        # Check that array will fit within current Arraylist
        new_array_length = len(array)
        if new_array_length > self._size - self._usage:
            raise ValueError
        else:
            new_array_counter = 0
            sparse_array_counter = 0

            while new_array_counter != new_array_length:
                if isinstance(self._data[sparse_array_counter], type(None)):
                    self.__setitem__(sparse_array_counter, array[new_array_counter])
                    new_array_counter += 1

                sparse_array_counter += 1
