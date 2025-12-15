import random


def random_data(n):
    return [random.randint(0, n) for _ in range(n)]


def sorted_data(n):
    return list(range(n))


def reversed_data(n):
    return list(range(n, 0, -1))


def almost_sorted_data(n, percent_sorted=0.95):
    arr = list(range(n))
    swaps = int(n * (1 - percent_sorted))
    for _ in range(swaps):
        i, j = random.sample(range(n), 2)
        arr[i], arr[j] = arr[j], arr[i]
    return arr
