import os


def binary_search(arr, target, left=0, right=None):
    """
    Временная сложность: O(log n)
    Глубина рекурсии: O(log n)
    """
    if right is None:
        right = len(arr) - 1
    if left > right:
        return -1

    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    if target < arr[mid]:
        return binary_search(arr, target, left, mid - 1)
    return binary_search(arr, target, mid + 1, right)


def traverse_fs(path, level=0, max_depth_tracker=None):
    """
    Временная сложность: O(n)
    Глубина рекурсии: O(d), где d — глубина каталогов
    """
    if max_depth_tracker is not None:
        max_depth_tracker[0] = max(max_depth_tracker[0], level)

    print("  " * level + os.path.basename(path))

    if not os.path.isdir(path):
        return

    for item in os.listdir(path):
        traverse_fs(os.path.join(path, item), level + 1, max_depth_tracker)


def hanoi(n, source, auxiliary, target, moves):
    """
    Временная сложность: O(2^n)
    Глубина рекурсии: O(n)
    """
    if n == 1:
        moves.append(f"{source} -> {target}")
        return
    hanoi(n - 1, source, target, auxiliary, moves)
    moves.append(f"{source} -> {target}")
    hanoi(n - 1, auxiliary, source, target, moves)
