class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Вставка значения в BST
        Средняя/Худшая сложность: O(log n) / O(n)"""
        if not self.root:
            self.root = TreeNode(value)
            return
        node = self.root
        while True:
            if value < node.value:
                if node.left:
                    node = node.left
                else:
                    node.left = TreeNode(value)
                    return
            else:
                if node.right:
                    node = node.right
                else:
                    node.right = TreeNode(value)
                    return

    def search(self, value):
        """Поиск значения в BST
        Средняя/Худшая сложность: O(log n) / O(n)"""
        node = self.root
        while node:
            if value == node.value:
                return node
            elif value < node.value:
                node = node.left
            else:
                node = node.right
        return None

    def find_min(self, node):
        """Поиск минимального значения в поддереве"""
        current = node
        while current.left:
            current = current.left
        return current

    def find_max(self, node):
        """Поиск максимального значения в поддереве"""
        current = node
        while current.right:
            current = current.right
        return current

    def delete(self, value):
        """Удаление узла из BST
        Средняя/Худшая сложность: O(log n) / O(n)"""
        self.root = self._delete_rec(self.root, value)

    def _delete_rec(self, node, value):
        if not node:
            return None
        if value < node.value:
            node.left = self._delete_rec(node.left, value)
        elif value > node.value:
            node.right = self._delete_rec(node.right, value)
        else:
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            temp = self.find_min(node.right)
            node.value = temp.value
            node.right = self._delete_rec(node.right, temp.value)
        return node

    def is_valid_bst(self):
        """Проверка корректности BST"""
        def validate(node, low, high):
            if not node:
                return True
            if not (low < node.value < high):
                return False
            return validate(node.left, low, node.value) and validate(node.right, node.value, high)
        return validate(self.root, float('-inf'), float('inf'))

    def height(self, node=None):
        """Вычисление высоты дерева"""
        if node is None:
            node = self.root
        if node is None:
            return 0
        left_height = self.height(node.left) if node.left else 0
        right_height = self.height(node.right) if node.right else 0
        return 1 + max(left_height, right_height)

    def visualize(self):
        """Текстовая визуализация дерева"""
        def _visual(node, indent=""):
            if not node:
                return ""
            result = _visual(node.right, indent + "   ")
            result += f"{indent}{node.value}\n"
            result += _visual(node.left, indent + "   ")
            return result
        print(_visual(self.root))
