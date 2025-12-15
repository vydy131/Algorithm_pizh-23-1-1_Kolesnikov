def bubble_sort(arr):
    """
    Время:
      худший: O(n^2)
      средний: O(n^2)
      лучший: O(n)
    Память: O(1)
    Устойчивая
    """
    a = arr.copy()
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a


def selection_sort(arr):
    """
    Время:
      худший: O(n^2)
      средний: O(n^2)
      лучший: O(n^2)
    Память: O(1)
    Неустойчивая
    """
    a = arr.copy()
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a


def insertion_sort(arr):
    """
    Время:
      худший: O(n^2)
      средний: O(n^2)
      лучший: O(n)
    Память: O(1)
    Устойчивая
    """
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


def merge_sort(arr):
    """
    Время:
      худший: O(n log n)
      средний: O(n log n)
      лучший: O(n log n)
    Память: O(n)
    Устойчивая
    """
    if len(arr) <= 1:
        return arr.copy()

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort(arr):
    """
    Время:
      худший: O(n^2)
      средний: O(n log n)
      лучший: O(n log n)
    Память: O(log n)
    Неустойчивая
    """
    if len(arr) <= 1:
        return arr.copy()

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)
