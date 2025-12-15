from hash_functions import hash_djb2, hash_polynomial


class HashTableLinearProbing:
    """
    Открытая адресация — линейное пробирование.
    Средний случай: O(1)
    Худший случай: O(n)
    """

    def __init__(self, size=8):
        self.size = size
        self.count = 0
        self.table = [None] * size

    def _hash(self, key, i):
        return (hash_djb2(key, self.size) + i) % self.size

    def insert(self, key, value):
        for i in range(self.size):
            idx = self._hash(key, i)
            if self.table[idx] is None or self.table[idx][0] == key:
                self.table[idx] = (key, value)
                self.count += 1
                return
        raise RuntimeError("Hash table overflow")

    def get(self, key):
        for i in range(self.size):
            idx = self._hash(key, i)
            if self.table[idx] is None:
                return None
            if self.table[idx][0] == key:
                return self.table[idx][1]
        return None


class HashTableDoubleHashing:
    """
    Открытая адресация — двойное хеширование.
    Средний случай: O(1)
    Худший случай: O(n)
    """

    def __init__(self, size=8):
        self.size = size
        self.count = 0
        self.table = [None] * size

    def _hash1(self, key):
        return hash_djb2(key, self.size)

    def _hash2(self, key):
        return 1 + hash_polynomial(key, self.size - 1)

    def insert(self, key, value):
        for i in range(self.size):
            idx = (self._hash1(key) + i * self._hash2(key)) % self.size
            if self.table[idx] is None or self.table[idx][0] == key:
                self.table[idx] = (key, value)
                self.count += 1
                return
        raise RuntimeError("Hash table overflow")

    def get(self, key):
        for i in range(self.size):
            idx = (self._hash1(key) + i * self._hash2(key)) % self.size
            if self.table[idx] is None:
                return None
            if self.table[idx][0] == key:
                return self.table[idx][1]
        return None
