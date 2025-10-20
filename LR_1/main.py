# search_comprasion.py
import timeit
import random
import matplotlib
matplotlib.use("Qt5Agg")
import matplotlib.pyplot as plt

def linear_search(arr, target):
    """Линейный поиск в массиве"""
    for i in range(0, len(arr)): # 0(N) - перебор массива данных
        if(arr[i] == target): # 0(1) - проверка на необходимый элемент
            return i # 0(1) - Возврат индекса найденного элемента
    return -1 # 0(1) - Если индекс не найден - вовращаем -1
    # Общая сложность алгоритма O(N) + O(1) + 0(1) = 0(N)

def binary_search(arr, target):
    """Бинарный поиск в отсортированном массиве"""
    left = 0 # 0(1) - положение крайнего левого элемента
    right = len(arr) - 1 # 0(1) - положение крайнего правого элемента

    while left <= right: # 0(log(n)) - алгоритм бинарного поиска
        mid = (left + right) // 2 # 0(1) высчитываем средний индекс
        if arr[mid] == target: # 0(1) проверяем на совпадения
            return mid  # 0(1) возвращаем индекс
        elif arr[mid] < target: # 0(1) если искомое больше среднего
            left = mid + 1 # 0(1) смещаем левую границу
        else:
            right = mid - 1 # 0(1) смещаем правую границу

    return -1  # Если элемент не найден
    # O(1) + O(1) + O(1) + O(1) + 0(log(n)) + O(1) = O(log(n)) - средняя скорость алгоритма с отсортированным массивом
    # 0(n log(n)) - средняя скорость алгоритма с сортировкой

# Функция для замера времени выполнения
def measure_time(func, data, target):
    """Измеряет время выполнения функции в миллисекундах."""
    start_time = timeit.default_timer()
    func(data, target)
    end_time = timeit.default_timer()
    return (end_time - start_time) * 1000

pc_info = """
Характеристики ПК для тестирования:
- Процессор: Intel Core i7-12400H @ 2.70GHz
- Оперативная память: 16 GB DDR4
- ОС: Windows 10
- Python: 3.13.1
"""

print(pc_info)

# Проведение экспериментов
sizes = [1000, 5000, 10000, 50000, 100000, 500000]
linear_times = []
binary_times = []
target = 1000

print("Замеры времени выполнения для алгоритма суммирования массива:")
print("{:>3} {:>12} {:>12} {:>15}".format("Алгоритм", "Размер (N)", "Время (мс)", "Время/N (мкс)"))
# Тестирование
for size in sizes:
    data = [random.randint(1, 1000) for _ in range(size)]
    data.sort()

    execution_time = timeit.timeit(lambda: linear_search(data, target), number=10) * 1000 / 10

    linear_times.append(execution_time)
    time_per_element = (execution_time * 1000) / size if size > 0 else 0 # мкс на элемент
    print("Linear: {:>10} {:>12.4f} {:>15.4f}".format(size, execution_time, time_per_element))

    execution_time = timeit.timeit(lambda: binary_search(data, target), number=10) * 1000 / 10

    binary_times.append(execution_time)
    time_per_element = (execution_time * 1000) / size if size > 0 else 0 # мкс на элемент

    print("Binary: {:>10} {:>12.4f} {:>15.4f}".format(size, execution_time, time_per_element))

plt.figure(figsize=(14, 6))
plt.subplot(1, 2, 1)
plt.plot(sizes, linear_times, 'bo-', label='Линейный поиск (O(N))', color="green")
plt.plot(sizes, binary_times, 'ro-', label='Бинарный поиск (O(log N))', color="red")
plt.xlabel('Размер массива (N)')
plt.ylabel('Время выполнения (мс)')
plt.title('Обычный масштаб')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(sizes, linear_times, 'bo-', label='Линейный поиск (O(N))', color="green")
plt.plot(sizes, binary_times, 'ro-', label='Бинарный поиск (O(log N))', color="red")
plt.yscale("log")
plt.xlabel('Размер массива (N)')
plt.ylabel('Время выполнения (мс, log scale)')
plt.title('Логарифмический масштаб по Y')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend()
plt.tight_layout()
plt.savefig('time_complexity_plot_5000.png', dpi=300, bbox_inches='tight')
plt.show()
