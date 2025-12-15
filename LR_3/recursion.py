def factorial(n):
    """
    Временная сложность: O(n)
    Глубина рекурсии: O(n)
    """
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    """
    Временная сложность: O(2^n)
    Глубина рекурсии: O(n)
    """
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def power(a, n):
    """
    Быстрое возведение в степень
    Временная сложность: O(log n)
    Глубина рекурсии: O(log n)
    """
    if n == 0:
        return 1
    if n % 2 == 0:
        half = power(a, n // 2)
        return half * half
    return a * power(a, n - 1)
