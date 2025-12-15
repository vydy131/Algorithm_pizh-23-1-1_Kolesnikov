import time
from dynamic_programming import fib_memo, fib_iter

def compare_fibonacci(n):
    start = time.time()
    fib_memo(n)
    t_memo = time.time()-start

    start = time.time()
    fib_iter(n)
    t_iter = time.time()-start

    print(f"Fibonacci({n}): Memo={t_memo:.6f}s, Iterative={t_iter:.6f}s")

if __name__=="__main__":
    ns=[10, 100, 500, 1000, 1500, 2000]
    for n in ns:
        compare_fibonacci(n)