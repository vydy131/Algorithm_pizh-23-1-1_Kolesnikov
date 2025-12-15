from performance_test import run_tests
from plot_results import plot_by_size, plot_by_data_type


def main():
    sizes = [100, 1000, 5000]
    results = run_tests(sizes)

    plot_by_size(results, "random")
    plot_by_data_type(results, 5000)


if __name__ == "__main__":
    main()
