import timeit
from collections import deque
import matplotlib.pyplot as plt
from linked_list import LinkedList

def measure_list_insert_start(n):
    lst = []
    for i in range(n):
        lst.insert(0, i)


def measure_linked_list_insert_start(n):
    ll = LinkedList()
    for i in range(n):
        ll.insert_at_start(i)


def measure_list_queue_pop(n):
    lst = list(range(n))
    for _ in range(n):
        lst.pop(0)


def measure_deque_queue_pop(n):
    dq = deque(range(n))
    for _ in range(n):
        dq.popleft()


def run_benchmarks():
    sizes = [100, 500, 1000, 2000, 5000]

    list_insert_times = []
    linked_insert_times = []

    list_pop_times = []
    deque_pop_times = []

    for n in sizes:
        t1 = timeit.timeit(lambda: measure_list_insert_start(n), number=1)
        t2 = timeit.timeit(lambda: measure_linked_list_insert_start(n), number=1)

        t3 = timeit.timeit(lambda: measure_list_queue_pop(n), number=1)
        t4 = timeit.timeit(lambda: measure_deque_queue_pop(n), number=1)

        list_insert_times.append(t1)
        linked_insert_times.append(t2)
        list_pop_times.append(t3)
        deque_pop_times.append(t4)

    return sizes, list_insert_times, linked_insert_times, list_pop_times, deque_pop_times


def plot_results(sizes, list_ins, ll_ins, list_pop, deque_pop):
    plt.figure()
    plt.plot(sizes, list_ins)
    plt.plot(sizes, ll_ins)
    plt.xlabel("Количество элементов")
    plt.ylabel("Время (сек)")
    plt.title("Вставка в начало: list vs LinkedList")
    plt.legend(["list (O(n))", "LinkedList (O(1))"])
    plt.grid()
    plt.show()

    plt.figure()
    plt.plot(sizes, list_pop)
    plt.plot(sizes, deque_pop)
    plt.xlabel("Количество элементов")
    plt.ylabel("Время (сек)")
    plt.title("Очередь: list.pop(0) vs deque.popleft()")
    plt.legend(["list (O(n))", "deque (O(1))"])
    plt.grid()
    plt.show()


if __name__ == "__main__":
    data = run_benchmarks()
    plot_results(*data)
