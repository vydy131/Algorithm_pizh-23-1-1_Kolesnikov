import random
import string
import timeit
import matplotlib.pyplot as plt

from hash_functions import hash_sum, hash_polynomial, hash_djb2
from hash_table_chaining import HashTableChaining
from hash_table_open_addressing import HashTableLinearProbing, HashTableDoubleHashing


def random_key(length=8):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))


def measure_table(table_cls, load_factors):
    results = []

    for lf in load_factors:
        table = table_cls(size=1000)
        n = int(table.size * lf)

        keys = [random_key() for _ in range(n)]
        time = timeit.timeit(
            lambda: [table.insert(k, k) for k in keys],
            number=1
        )
        results.append(time)

    return results


def plot_load_factor(load_factors, *results, labels):
    for r, label in zip(results, labels):
        plt.plot(load_factors, r)

    plt.xlabel("Коэффициент заполнения")
    plt.ylabel("Время (сек)")
    plt.title("Производительность хеш-таблиц")
    plt.legend(labels)
    plt.grid()
    plt.show()


def plot_hash_distribution(hash_fn, title):
    size = 100
    keys = [random_key() for _ in range(1000)]
    buckets = [0] * size

    for k in keys:
        buckets[hash_fn(k, size)] += 1

    plt.bar(range(size), buckets)
    plt.title(title)
    plt.xlabel("Индекс")
    plt.ylabel("Количество")
    plt.show()


if __name__ == "__main__":
    load_factors = [0.1, 0.5, 0.7, 0.9]

    chaining = measure_table(HashTableChaining, load_factors)
    linear = measure_table(HashTableLinearProbing, load_factors)
    double = measure_table(HashTableDoubleHashing, load_factors)

    plot_load_factor(
        load_factors,
        chaining,
        linear,
        double,
        labels=["Chaining", "Linear probing", "Double hashing"]
    )

    plot_hash_distribution(hash_sum, "Hash Sum")
    plot_hash_distribution(hash_polynomial, "Polynomial Hash")
    plot_hash_distribution(hash_djb2, "DJB2 Hash")
