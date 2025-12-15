from hash_table_chaining import HashTableChaining
from hash_table_open_addressing import HashTableLinearProbing, HashTableDoubleHashing


def run_tests():
    tables = [
        HashTableChaining(),
        HashTableLinearProbing(),
        HashTableDoubleHashing()
    ]

    for table in tables:
        table.insert("a", 1)
        table.insert("b", 2)
        table.insert("a", 3)

        assert table.get("a") == 3
        assert table.get("b") == 2
        assert table.get("c") is None


if __name__ == "__main__":
    run_tests()
    print("All tests passed")
