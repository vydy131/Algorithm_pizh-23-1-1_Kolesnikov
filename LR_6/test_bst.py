import unittest
import sys
import os
sys.path.append(os.path.dirname(__file__))
from tree_traversal import inorder_recursive, preorder_recursive, postorder_recursive, inorder_iterative
from binary_search_tree import BinarySearchTree


class TestBST(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()
        for v in [50, 30, 70, 20, 40, 60, 80]:
            self.bst.insert(v)

    def test_insert_search(self):
        self.assertIsNotNone(self.bst.search(50))
        self.assertIsNone(self.bst.search(100))

    def test_delete(self):
        self.bst.delete(70)
        self.assertIsNone(self.bst.search(70))
        self.assertTrue(self.bst.is_valid_bst())

    def test_traversals(self):
        self.assertEqual(list(inorder_recursive(self.bst.root)), [20, 30, 40, 50, 60, 70, 80])
        self.assertEqual(list(preorder_recursive(self.bst.root)), [50, 30, 20, 40, 70, 60, 80])
        self.assertEqual(list(postorder_recursive(self.bst.root)), [20, 40, 30, 60, 80, 70, 50])
        self.assertEqual(list(inorder_iterative(self.bst.root)), [20, 30, 40, 50, 60, 70, 80])

if __name__ == "__main__":
    unittest.main()