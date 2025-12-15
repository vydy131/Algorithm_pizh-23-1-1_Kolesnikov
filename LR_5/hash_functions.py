def hash_sum(key: str, size: int) -> int:
    """
    Простая хеш-функция.
    Плюс: простота.
    Минус: плохое распределение.
    """
    return sum(ord(c) for c in key) % size


def hash_polynomial(key: str, size: int, base=31) -> int:
    """
    Полиномиальный хеш.
    Хорошее распределение для строк.
    """
    h = 0
    for c in key:
        h = h * base + ord(c)
    return h % size


def hash_djb2(key: str, size: int) -> int:
    """
    DJB2.
    Хорошее распределение, часто используется на практике.
    """
    h = 5381
    for c in key:
        h = ((h << 5) + h) + ord(c)
    return h % size
