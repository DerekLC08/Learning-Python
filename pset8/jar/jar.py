class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Invalid Capacity")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return ("🍪" * self.size)

    def deposit(self, n):
        if n > self.capacity:
            raise ValueError("Size is larger than capacity")
        if self.size + n > self.capacity:
            raise ValueError("New size exceeds capacity")
        self._size += n


    def withdraw(self, n):
        if self.size < n:
            raise ValueError("Jar cannot have negative cookies")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size