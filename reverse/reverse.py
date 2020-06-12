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

        if node is not None:

            nxt = node.next_node  # equal to 4

            node.next_node = prev  # equal to none
            self.reverse_list(nxt, node)

        else:
            self.head = prev


test_list = LinkedList()

test_list.add_to_head(1)
test_list.add_to_head(2)
test_list.add_to_head(3)
test_list.add_to_head(4)
test_list.add_to_head(5)
# 5,4,3,2,1
# we want it to be 1,2,3,4,5
# head should be 1
print(test_list.head.value)
test_list.reverse_list(test_list.head, None)
