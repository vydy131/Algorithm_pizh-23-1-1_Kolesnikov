import matplotlib.pyplot as plt


def plot_by_size(results, data_type):
    sizes = sorted(results.keys())
    algorithms = results[sizes[0]][data_type].keys()

    for algo in algorithms:
        times = [results[size][data_type][algo] for size in sizes]
        plt.plot(sizes, times)

    plt.xlabel("Размер массива")
    plt.ylabel("Время (сек)")
    plt.title(f"Сортировки на данных типа: {data_type}")
    plt.legend(algorithms)
    plt.grid()
    plt.show()


def plot_by_data_type(results, size):
    data_types = results[size].keys()
    algorithms = results[size][next(iter(data_types))].keys()

    for algo in algorithms:
        times = [results[size][dt][algo] for dt in data_types]
        plt.plot(list(data_types), times)

    plt.xlabel("Тип данных")
    plt.ylabel("Время (сек)")
    plt.title(f"Сортировки для n = {size}")
    plt.legend(algorithms)
    plt.grid()
    plt.show()
