class Heap:
    def __init__(self, is_min=True):
        self.data = []
        self.is_min = is_min

    def _compare(self, a, b):
        return a < b if self.is_min else a > b

    def _sift_up(self, index):
        """Всплытие элемента
        Сложность: O(log n)"""
        parent = (index - 1) // 2
        while index > 0 and self._compare(self.data[index], self.data[parent]):
            self.data[index], self.data[parent] = self.data[parent], self.data[index]
            index = parent
            parent = (index - 1) // 2

    def _sift_down(self, index):
        """Погружение элемента
        Сложность: O(log n)"""
        n = len(self.data)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest_largest = index

            if left < n and self._compare(self.data[left], self.data[smallest_largest]):
                smallest_largest = left
            if right < n and self._compare(self.data[right], self.data[smallest_largest]):
                smallest_largest = right
            if smallest_largest == index:
                break
            self.data[index], self.data[smallest_largest] = self.data[smallest_largest], self.data[index]
            index = smallest_largest

    def insert(self, value):
        """Вставка элемента
        Сложность: O(log n)"""
        self.data.append(value)
        self._sift_up(len(self.data) - 1)

    def extract(self):
        """Извлечение корня
        Сложность: O(log n)"""
        if not self.data:
            return None
        root = self.data[0]
        last = self.data.pop()
        if self.data:
            self.data[0] = last
            self._sift_down(0)
        return root

    def peek(self):
        """Просмотр корня
        Сложность: O(1)"""
        return self.data[0] if self.data else None

    def build_heap(self, array):
        """Построение кучи из массива
        Сложность: O(n)"""
        self.data = array[:]
        for i in reversed(range(len(self.data) // 2)):
            self._sift_down(i)

    def __len__(self):
        return len(self.data)

    def visualize(self):
        """Текстовая визуализация дерева (для небольших куч)"""
        def _visual(idx, indent=""):
            if idx >= len(self.data):
                return ""
            result = _visual(2 * idx + 2, indent + "   ")
            result += f"{indent}{self.data[idx]}\n"
            result += _visual(2 * idx + 1, indent + "   ")
            return result
        print(_visual(0))
