from heap import Heap

def heapsort(array, is_min=True):
    """In-place Heapsort
    Сложность: O(n log n)"""
    heap = Heap(is_min=is_min)
    heap.build_heap(array)
    sorted_array = []
    while len(heap):
        sorted_array.append(heap.extract())
    if is_min:
        return sorted_array
    else:
        return sorted_array[::-1]

def heapsort_inplace(array):
    """In-place Heapsort без дополнительного массива
    Сложность: O(n log n)"""
    n = len(array)

    # Превращаем массив в max-кучу
    for i in reversed(range(n // 2)):
        _sift_down(array, i, n)

    # Сортировка
    for end in reversed(range(1, n)):
        array[0], array[end] = array[end], array[0]
        _sift_down(array, 0, end)
    return array

def _sift_down(arr, start, end):
    root = start
    while 2 * root + 1 < end:
        child = 2 * root + 1
        swap = root
        if arr[swap] < arr[child]:
            swap = child
        if child + 1 < end and arr[swap] < arr[child + 1]:
            swap = child + 1
        if swap == root:
            return
        arr[root], arr[swap] = arr[swap], arr[root]
        root = swap
