import time
from greedy_algorithms import interval_scheduling, fractional_knapsack, min_coins, huffman_coding
import random
import matplotlib.pyplot as plt

def experiment_knapsack():
    sizes = [10, 50, 100, 500, 1000]
    times = []
    for n in sizes:
        items = [(random.randint(10,100), random.randint(1,50)) for _ in range(n)]
        capacity = 1000
        start = time.time()
        fractional_knapsack(items, capacity)
        times.append(time.time() - start)
    plt.plot(sizes, times, marker='o')
    plt.xlabel("Number of items")
    plt.ylabel("Time (s)")
    plt.title("Fractional Knapsack Performance")
    plt.grid(True)
    plt.show()

def experiment_huffman():
    sizes = [100, 500, 1000, 5000, 10000]
    times = []
    for n in sizes:
        symbols = {chr(65+i): random.randint(1,100) for i in range(n)}
        start = time.time()
        huffman_coding(symbols)
        times.append(time.time() - start)
    plt.plot(sizes, times, marker='o', color='red')
    plt.xlabel("Number of symbols")
    plt.ylabel("Time (s)")
    plt.title("Huffman Coding Performance")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    # Примеры работы
    intervals = [(1,3),(2,5),(4,7),(6,9)]
    print("Interval Scheduling:", interval_scheduling(intervals))

    items = [(60,10),(100,20),(120,30)]
    value, fractions = fractional_knapsack(items, 50)
    print("Fractional Knapsack Value:", value)
    print("Fractions taken:", fractions)

    amount = 87
    print("Minimum coins for", amount, ":", min_coins(amount))

    freq = {'a':5,'b':9,'c':12,'d':13,'e':16,'f':45}
    codes, _ = huffman_coding(freq)
    print("Huffman Codes:", codes)

    experiment_knapsack()
    experiment_huffman()