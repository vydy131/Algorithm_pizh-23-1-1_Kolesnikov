import time


class FibCounter:
    def __init__(self):
        self.calls = 0


def fib_naive(n, counter):
    counter.calls += 1
    if n <= 1:
        return n
    return fib_naive(n - 1, counter) + fib_naive(n - 2, counter)


def fib_memo(n, memo, counter):
    counter.calls += 1
    if n in memo:
        return memo[n]
    if n <= 1:
        memo[n] = n
    else:
        memo[n] = fib_memo(n - 1, memo, counter) + fib_memo(n - 2, memo, counter)
    return memo[n]


def compare_fibonacci(n=35):
    counter_naive = FibCounter()
    counter_memo = FibCounter()

    start = time.perf_counter()
    fib_naive(n, counter_naive)
    naive_time = time.perf_counter() - start

    start = time.perf_counter()
    fib_memo(n, {}, counter_memo)
    memo_time = time.perf_counter() - start

    return {
        "naive_time": naive_time,
        "memo_time": memo_time,
        "naive_calls": counter_naive.calls,
        "memo_calls": counter_memo.calls
    }
