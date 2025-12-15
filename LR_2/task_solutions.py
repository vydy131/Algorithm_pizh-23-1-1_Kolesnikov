from collections import deque


def check_brackets(sequence):
    """Стек на list, O(n)"""
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for ch in sequence:
        if ch in '([{':
            stack.append(ch)
        elif ch in ')]}':
            if not stack or stack.pop() != pairs[ch]:
                return False
    return not stack


def print_queue_simulation(tasks):
    """Очередь печати на deque, O(n)"""
    queue = deque(tasks)
    result = []

    while queue:
        task = queue.popleft()
        result.append(f"Печать: {task}")

    return result


def is_palindrome(sequence):
    """Дек, O(n)"""
    dq = deque(sequence)

    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True


if __name__ == "__main__":
    print("Проверка скобок:")
    print(check_brackets("{[()()]}"))
    print(check_brackets("{[(])}"))

    print("\nОчередь печати:")
    for line in print_queue_simulation(["doc1", "doc2", "doc3"]):
        print(line)

    print("\nПалиндром:")
    print(is_palindrome("radar"))
    print(is_palindrome("python"))
