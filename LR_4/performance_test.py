import timeit
from sorts import (
    bubble_sort,
    selection_sort,
    insertion_sort,
    merge_sort,
    quick_sort
)
from generate_data import (
    random_data,
    sorted_data,
    reversed_data,
    almost_sorted_data
)


SORTS = {
    "bubble": bubble_sort,
    "selection": selection_sort,
    "insertion": insertion_sort,
    "merge": merge_sort,
    "quick": quick_sort
}

DATASETS = {
    "random": random_data,
    "sorted": sorted_data,
    "reversed": reversed_data,
    "almost_sorted": almost_sorted_data
}


def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


def run_tests(sizes):
    results = {}

    for size in sizes:
        results[size] = {}
        for data_name, data_fn in DATASETS.items():
            base_data = data_fn(size)
            results[size][data_name] = {}

            for sort_name, sort_fn in SORTS.items():
                data_copy = base_data.copy()
                time = timeit.timeit(lambda: sort_fn(data_copy), number=1)
                sorted_result = sort_fn(data_copy)

                assert is_sorted(sorted_result)

                results[size][data_name][sort_name] = time

    return results
