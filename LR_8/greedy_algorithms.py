import heapq

def interval_scheduling(intervals):
    """
    Выбирает максимальное число непересекающихся интервалов.
    Жадный выбор: сортировка по времени окончания.
    Сложность: O(n log n)
    """
    sorted_intervals = sorted(intervals, key=lambda x: x[1])
    result = []
    end_time = float('-inf')
    for start, end in sorted_intervals:
        if start >= end_time:
            result.append((start, end))
            end_time = end
    return result


def fractional_knapsack(items, capacity):
    """
    items: список кортежей (value, weight)
    capacity: максимальный вес
    Жадный выбор: сортировка по удельной стоимости value/weight
    Сложность: O(n log n)
    """
    items = sorted(items, key=lambda x: x[0]/x[1], reverse=True)
    total_value = 0
    fractions = []
    for value, weight in items:
        if capacity >= weight:
            capacity -= weight
            total_value += value
            fractions.append((value, weight, 1))
        else:
            fraction = capacity / weight
            total_value += value * fraction
            fractions.append((value, weight, fraction))
            break
    return total_value, fractions


class HuffmanNode:
    def __init__(self, freq, symbol=None, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
    def __lt__(self, other):
        return self.freq < other.freq

def huffman_coding(freq_dict):
    """
    Строит оптимальный префиксный код Хаффмана
    Сложность: O(n log n)
    """
    heap = [HuffmanNode(f, s) for s, f in freq_dict.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        merged = HuffmanNode(a.freq + b.freq, left=a, right=b)
        heapq.heappush(heap, merged)
    root = heap[0]

    codes = {}
    def generate_codes(node, prefix=""):
        if node.symbol is not None:
            codes[node.symbol] = prefix
            return
        generate_codes(node.left, prefix + "0")
        generate_codes(node.right, prefix + "1")
    generate_codes(root)
    return codes, root


def min_coins(amount, coins=[1,2,5,10,20,50,100,200]):
    """
    Жадный алгоритм для стандартной системы монет
    Сложность: O(n)
    """
    coins = sorted(coins, reverse=True)
    result = []
    for coin in coins:
        while amount >= coin:
            amount -= coin
            result.append(coin)
    return result
