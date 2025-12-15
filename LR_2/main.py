from linked_list import LinkedList
from performance_analysis import run_benchmarks, plot_results
from task_solutions import (
    check_brackets,
    print_queue_simulation,
    is_palindrome
)


def demo_linked_list():
    print("=== LinkedList ===")
    ll = LinkedList()

    ll.insert_at_start(3)
    ll.insert_at_start(2)
    ll.insert_at_start(1)
    ll.insert_at_end(4)
    ll.insert_at_end(5)

    print("Список после вставок:", ll.traversal())

    removed = ll.delete_from_start()
    print("Удалён элемент:", removed)
    print("Список после удаления:", ll.traversal())


def demo_tasks():
    print("\n=== Практические задачи ===")

    print("\n1. Проверка скобок")
    print("{[()()]} ->", check_brackets("{[()()]}"))
    print("{[(])} ->", check_brackets("{[(])}"))

    print("\n2. Очередь печати")
    tasks = ["report.pdf", "image.png", "notes.txt"]
    for result in print_queue_simulation(tasks):
        print(result)

    print("\n3. Палиндром")
    print("radar ->", is_palindrome("radar"))
    print("python ->", is_palindrome("python"))


def demo_performance():
    print("\n=== Анализ производительности ===")
    sizes, list_ins, ll_ins, list_pop, deque_pop = run_benchmarks()
    plot_results(sizes, list_ins, ll_ins, list_pop, deque_pop)


def main():
    demo_linked_list()
    demo_tasks()
    demo_performance()


if __name__ == "__main__":
    main()
