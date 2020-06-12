class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # make a new BSTNode with our value

        if value < self.value:
            if not self.left:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)

        if value >= self.value:
            if not self.right:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):

        if target == self.value:
            return True

        elif target < self.value:
            if not self.left:
                return False
            elif self.left:
                if self.left.contains(target):
                    return True

        elif target > self.value:
            if not self.right:
                return False
            elif self.right:
                if self.right.contains(target):
                    return True

        else:
            return False

    # Return the maximum value found in the tree
    def get_max(self):

        if not self.right:
            max_value = self.value

            return max_value

        elif self.value <= self.right.value:
            max_value = self.right.get_max()

            return max_value

        # if self.right is None:
        #     return self.value
        # else:
        #     return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)

        if self.right:
            self.right.for_each(fn)
        if self.left:
            self.left.for_each(fn)
