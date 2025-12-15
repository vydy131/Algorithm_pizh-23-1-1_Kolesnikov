def inorder_recursive(node):
    if node:
        yield from inorder_recursive(node.left)
        yield node.value
        yield from inorder_recursive(node.right)

def preorder_recursive(node):
    if node:
        yield node.value
        yield from preorder_recursive(node.left)
        yield from preorder_recursive(node.right)

def postorder_recursive(node):
    if node:
        yield from postorder_recursive(node.left)
        yield from postorder_recursive(node.right)
        yield node.value

def inorder_iterative(root):
    stack = []
    node = root
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        yield node.value
        node = node.right