import matplotlib.pyplot as plt
import random
import time

from binary_search_tree import BinarySearchTree
from tree_traversal import inorder_recursive, preorder_recursive, postorder_recursive, inorder_iterative


def measure_search_time(tree, values):
    start = time.time()
    for val in values:
        tree.search(val)
    return time.time() - start

def experiment():
    sizes = [100, 500, 1000, 2000, 5000]
    balanced_times = []
    degenerate_times = []

    for n in sizes:
        # Сбалансированное дерево
        bst = BinarySearchTree()
        elems = list(range(n))
        random.shuffle(elems)
        for e in elems:
            bst.insert(e)
        search_vals = random.choices(elems, k=1000)
        t = measure_search_time(bst, search_vals)
        balanced_times.append(t)

        # Вырожденное дерево (отсортированные элементы)
        bst2 = BinarySearchTree()
        for e in range(n):
            bst2.insert(e)
        search_vals2 = random.choices(range(n), k=1000)
        t2 = measure_search_time(bst2, search_vals2)
        degenerate_times.append(t2)

    plt.plot(sizes, balanced_times, label="Balanced BST")
    plt.plot(sizes, degenerate_times, label="Degenerate BST")
    plt.xlabel("Number of nodes")
    plt.ylabel("Time for 1000 searches (s)")
    plt.title("Search Time in BSTs")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    experiment()

    bst = BinarySearchTree()
    for v in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(v)

    print("In-order Recursive:", list(inorder_recursive(bst.root)))
    print("Pre-order Recursive:", list(preorder_recursive(bst.root)))
    print("Post-order Recursive:", list(postorder_recursive(bst.root)))
    print("In-order Iterative:", list(inorder_iterative(bst.root)))
    print("BST is valid:", bst.is_valid_bst())
    print("Height:", bst.height())
    print("Tree visualization:")
    bst.visualize()
