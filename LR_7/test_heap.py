import unittest
import sys
import os
sys.path.append(os.path.dirname(__file__))
from heap import Heap
from heapsort import heapsort, heapsort_inplace
from priority_queue import PriorityQueue

class TestHeap(unittest.TestCase):
    def test_min_heap(self):
        h = Heap(is_min=True)
        for v in [5, 3, 8, 1, 6]:
            h.insert(v)
        self.assertEqual(h.extract(), 1)
        self.assertEqual(h.extract(), 3)

    def test_build_heap(self):
        arr = [4, 7, 1, 9, 2]
        h = Heap()
        h.build_heap(arr)
        self.assertEqual(h.extract(), 1)

    def test_heapsort(self):
        arr = [5, 2, 8, 1, 3]
        sorted_arr = heapsort(arr)
        self.assertEqual(sorted_arr, [1, 2, 3, 5, 8])
        arr2 = [5, 2, 8, 1, 3]
        heapsort_inplace(arr2)
        self.assertEqual(arr2, [1, 2, 3, 5, 8])

    def test_priority_queue(self):
        pq = PriorityQueue()
        pq.enqueue("low", 1)
        pq.enqueue("high", 5)
        pq.enqueue("medium", 3)
        self.assertEqual(pq.dequeue(), "high")
        self.assertEqual(pq.dequeue(), "medium")
        self.assertEqual(pq.dequeue(), "low")

if __name__ == "__main__":
    unittest.main()