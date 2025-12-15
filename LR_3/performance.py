import timeit
import matplotlib.pyplot as plt
from recursion import fibonacci
from memoization import fib_memo, FibCounter


def measure_fib_times():
    ns = [5, 10, 15, 20, 25, 30]
    naive_times = []
    memo_times = []

    for n in ns:
        naive_times.append(
            timeit.timeit(lambda: fibonacci(n), number=1)
        )

        counter = FibCounter()
        memo_times.append(
            timeit.timeit(lambda: fib_memo(n, {}, counter), number=1)
        )

    return ns, naive_times, memo_times


def plot_fibonacci(ns, naive, memo):
    plt.figure()
    plt.plot(ns, naive)
    plt.plot(ns, memo)
    plt.xlabel("n")
    plt.ylabel("Время (сек)")
    plt.title("Фибоначчи: наивная рекурсия vs мемоизация")
    plt.legend(["Наивная", "С мемоизацией"])
    plt.grid()
    plt.show()


if __name__ == "__main__":
    ns, naive, memo = measure_fib_times()
    plot_fibonacci(ns, naive, memo)
