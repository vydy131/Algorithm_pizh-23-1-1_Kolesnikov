from recursion import factorial, fibonacci, power
from memoization import compare_fibonacci
from recursion_tasks import binary_search, hanoi
from performance import measure_fib_times, plot_fibonacci


def main():
    print("Факториал 5:", factorial(5))
    print("Фибоначчи 10:", fibonacci(10))
    print("2^10:", power(2, 10))

    print("\nСравнение Фибоначчи (n=35):")
    stats = compare_fibonacci()
    for k, v in stats.items():
        print(f"{k}: {v}")

    print("\nБинарный поиск:")
    arr = list(range(1, 21))
    print("Индекс 13:", binary_search(arr, 13))

    print("\nХанойские башни (n=3):")
    moves = []
    hanoi(3, "A", "B", "C", moves)
    for move in moves:
        print(move)

    print("\nГрафик производительности Фибоначчи:")
    ns, naive, memo = measure_fib_times()
    plot_fibonacci(ns, naive, memo)


if __name__ == "__main__":
    main()
