from hash_functions import hash_djb2


class HashTableChaining:
    """
    Метод цепочек.
    Вставка / поиск / удаление:
      средний случай: O(1)
      худший случай: O(n)
    """

    def __init__(self, size=8, load_factor=0.75, hash_fn=hash_djb2):
        self.size = size
        self.count = 0
        self.load_factor = load_factor
        self.hash_fn = hash_fn
        self.table = [[] for _ in range(size)]

    def _resize(self):
        old = self.table
        self.size *= 2
        self.table = [[] for _ in range(self.size)]
        self.count = 0
        for bucket in old:
            for k, v in bucket:
                self.insert(k, v)

    def insert(self, key, value):
        if self.count / self.size > self.load_factor:
            self._resize()

        idx = self.hash_fn(key, self.size)
        bucket = self.table[idx]

        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))
        self.count += 1

    def get(self, key):
        idx = self.hash_fn(key, self.size)
        for k, v in self.table[idx]:
            if k == key:
                return v
        return None

    def delete(self, key):
        idx = self.hash_fn(key, self.size)
        bucket = self.table[idx]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.count -= 1
                return True
        return False
