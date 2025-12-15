import time
import matplotlib.pyplot as plt
from dynamic_programming import (
    fib_recursive, fib_memo, fib_iter,
    knapsack_01, lcs, levenshtein,
    coin_change, lis
)

def demo_fibonacci(n):
    print(f"\n=== Fibonacci({n}) ===")
    start = time.time()
    print("Memoization:", fib_memo(n))
    print("Time:", time.time()-start)

    start = time.time()
    print("Iterative:", fib_iter(n))
    print("Time:", time.time()-start)


def demo_knapsack():
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 50
    total, items = knapsack_01(weights, values, capacity)
    print(f"\n=== 0-1 Knapsack Capacity={capacity} ===")
    print("Max value:", total)
    print("Items selected:", items)


def demo_lcs():
    X, Y = "AGGTAB", "GXTXAYB"
    length, seq = lcs(X, Y)
    print(f"\n=== LCS of {X} and {Y} ===")
    print("Length:", length)
    print("Sequence:", seq)


def demo_levenshtein():
    s1, s2 = "kitten", "sitting"
    dist = levenshtein(s1, s2)
    print(f"\n=== Levenshtein distance between {s1} and {s2} ===")
    print("Distance:", dist)


def demo_coin_change():
    coins = [1, 2, 5, 10, 20, 50, 100]
    amount = 87
    min_num = coin_change(coins, amount)
    print(f"\n=== Coin Change for {amount} ===")
    print("Minimum coins:", min_num)


def demo_lis():
    arr = [10, 22, 9, 33, 21, 50, 41, 60]
    length, seq = lis(arr)
    print(f"\n=== Longest Increasing Subsequence of {arr} ===")
    print("Length:", length)
    print("Sequence:", seq)


def fibonacci_performance():
    ns = [10, 100, 500, 1000, 1500, 2000]
    times_memo = []
    times_iter = []
    for n in ns:
        start = time.time()
        fib_memo(n)
        times_memo.append(time.time()-start)

        start = time.time()
        fib_iter(n)
        times_iter.append(time.time()-start)

    plt.plot(ns, times_memo, marker='o', label="Memoization")
    plt.plot(ns, times_iter, marker='x', label="Iterative")
    plt.xlabel("n")
    plt.ylabel("Time (s)")
    plt.title("Fibonacci Performance")
    plt.grid(True)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    demo_fibonacci(30)
    demo_knapsack()
    demo_lcs()
    demo_levenshtein()
    demo_coin_change()
    demo_lis()
    fibonacci_performance()