from heap import Heap

class PriorityQueue:
    def __init__(self):
        self.heap = Heap(is_min=False)  # max-heap для приоритетов
        self.counter = 0  # для сохранения FIFO при одинаковых приоритетах

    def enqueue(self, item, priority):
        """Добавление элемента с приоритетом
        Сложность: O(log n)"""
        self.heap.insert((priority, self.counter, item))
        self.counter += 1

    def dequeue(self):
        """Извлечение элемента с наивысшим приоритетом
        Сложность: O(log n)"""
        if len(self.heap) == 0:
            return None
        return self.heap.extract()[2]

    def peek(self):
        """Просмотр элемента с наивысшим приоритетом"""
        if len(self.heap) == 0:
            return None
        return self.heap.peek()[2]