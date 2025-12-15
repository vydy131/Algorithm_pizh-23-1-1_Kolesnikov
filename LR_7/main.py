from heap import Heap
from heapsort import heapsort, heapsort_inplace
from priority_queue import PriorityQueue
import time
import random
import matplotlib.pyplot as plt

def demo_heap():
    print("=== Демонстрация MinHeap ===")
    h = Heap(is_min=True)
    for v in [5, 3, 8, 1, 6]:
        h.insert(v)
    print("Heap после вставки:", h.data)
    print("Корень:", h.peek())
    print("Извлечение элементов по порядку:")
    while len(h):
        print(h.extract(), end=" ")
    print("\n")

def demo_build_heap():
    print("=== Построение кучи из массива ===")
    arr = [4, 7, 1, 9, 2]
    h = Heap()
    h.build_heap(arr)
    print("Heap после build_heap:", h.data)
    print("Визуализация дерева:")
    h.visualize()
    print()

def demo_heapsort():
    print("=== Heapsort ===")
    arr = [5, 2, 8, 1, 3]
    sorted_arr = heapsort(arr)
    print("Исходный массив:", arr)
    print("Отсортированный (Heapsort):", sorted_arr)
    arr2 = [5, 2, 8, 1, 3]
    heapsort_inplace(arr2)
    print("Отсортированный in-place:", arr2)
    print()

def demo_priority_queue():
    print("=== Приоритетная очередь ===")
    pq = PriorityQueue()
    pq.enqueue("low", 1)
    pq.enqueue("high", 5)
    pq.enqueue("medium", 3)
    print("Извлечение элементов по приоритету:")
    while pq.peek() is not None:
        print(pq.dequeue(), end=" ")
    print("\n")

def demo_experiment():
    print("=== Время операций с кучей и сортировок ===")
    sizes = [1000, 5000, 10000, 20000, 50000]
    insert_times, build_times, heapsort_times, quicksort_times, mergesort_times = [], [], [], [], []

    for n in sizes:
        arr = [random.randint(0, n) for _ in range(n)]

        h = Heap()
        start = time.time()
        for v in arr:
            h.insert(v)
        insert_times.append(time.time() - start)

        h2 = Heap()
        start = time.time()
        h2.build_heap(arr)
        build_times.append(time.time() - start)

        start = time.time()
        heapsort(arr)
        heapsort_times.append(time.time() - start)

        arr_qs = arr[:]
        start = time.time()
        arr_qs.sort()
        quicksort_times.append(time.time() - start)

        arr_ms = arr[:]
        start = time.time()
        sorted(arr_ms)
        mergesort_times.append(time.time() - start)

    plt.plot(sizes, insert_times, label="Insert sequential")
    plt.plot(sizes, build_times, label="Build heap")
    plt.plot(sizes, heapsort_times, label="Heapsort")
    plt.plot(sizes, quicksort_times, label="QuickSort")
    plt.plot(sizes, mergesort_times, label="MergeSort")
    plt.xlabel("Number of elements")
    plt.ylabel("Time (s)")
    plt.title("Heap Operations and Sorting Comparison")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    demo_heap()
    demo_build_heap()
    demo_heapsort()
    demo_priority_queue()
    demo_experiment()
