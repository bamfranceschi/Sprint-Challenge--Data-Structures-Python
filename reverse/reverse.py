class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def __repr__(self):
        return f"{self.value}"

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):

        if node is None:
            return None

        prev = None

        if node.next_node:
            self.reverse_list(node.next_node, node)

        if prev:
            node.next_node = prev

        elif prev is None:
            node.next_node = None


test_list = LinkedList()

test_list.add_to_head(1)
print(test_list.head.value)
test_list.add_to_head(2)
print(test_list.head.value)
test_list.add_to_head(3)
print(test_list.head.value)
test_list.add_to_head(4)
print(test_list.head.value)
test_list.add_to_head(5)
print(test_list.head.value)

test_list.reverse_list(test_list.head, None)
print(test_list.head.value)
