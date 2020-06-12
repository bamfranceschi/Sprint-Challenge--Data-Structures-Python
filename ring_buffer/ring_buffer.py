class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None for i in range(capacity)]
        self.start = self.end = -1

    def __len__(self):
        return len(self.buffer)

    def __repr__(self):

        return f"{self.buffer}"

    def append(self, item):

        if self.start == -1:
            self.start = 0
            self.end = 0
            self.buffer[self.end] = item

        else:
            self.end = (self.end + 1) % self.capacity
            self.buffer[self.end] = item

    def get(self):

        return self.buffer


ring = RingBuffer(5)

ring.append("a")
print(ring)
ring.append("b")
print(ring)
ring.append("c")
print(ring)
ring.append("d")
print(ring)
ring.append("e")
print(ring)
ring.append("f")
print(ring)
