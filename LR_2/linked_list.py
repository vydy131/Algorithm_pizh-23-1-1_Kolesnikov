class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_start(self, value):
        """O(1)"""
        node = Node(value)
        node.next = self.head
        self.head = node
        if self.tail is None:
            self.tail = node

    def insert_at_end(self, value):
        """O(1)"""
        node = Node(value)
        if self.tail is None:
            self.head = self.tail = node
            return
        self.tail.next = node
        self.tail = node

    def delete_from_start(self):
        """O(1)"""
        if self.head is None:
            return None
        value = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return value

    def traversal(self):
        """O(n)"""
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result
