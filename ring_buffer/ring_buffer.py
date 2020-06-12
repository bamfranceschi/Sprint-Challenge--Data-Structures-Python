class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.oldest = oldest
        self.newest = newest  # where we write
        self.buffer = []

    def __len__(self):
        return len(self.buffer)

    def __repr__(self):

        return f"{self.buffer}"

    def append(self, item):
        self.oldest = self.buffer[0]
        self.newest = self.buffer[0]
        # understand if buffer is empty
        if len(self.buffer) == 0:
            # if buffer is not empty, add item
            self.buffer.append(item)
            self.oldest = self.buffer[0]
            self.newest = self.buffer[0]
        # if buffer is at capacity, overwrite oldest item with new item
        if len(self.buffer) < self.capacity:
            self.buffer.append(item)
            self.newest = self.buffer[item]
            print(self.newest)

        # if len(self.buffer) == self.capacity:

            # if buffer.length = capacity:
            #buffer.oldest = item

    def get(self):
        # if buffer is empty, return empty array
        # if buffer is not empty, return all values in capacity, except when value is none
        return self.buffer


ring = RingBuffer(5)

ring.append("a")
ring.append("b")
ring.append("c")
ring.append("d")

print(ring)
