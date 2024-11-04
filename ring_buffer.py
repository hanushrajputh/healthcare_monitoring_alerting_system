class RingBuffer:
    def __init__(self, size):
        self.size = size
        self.buffer = [None] * size
        self.index = 0
        self.count = 0

    def insert(self, data):
        self.buffer[self.index] = data
        self.index = (self.index + 1) % self.size
        if self.count < self.size:
            self.count += 1

    def get_data(self):
        if self.count == self.size:
            return self.buffer[self.index:] + self.buffer[:self.index]
        else:
            return self.buffer[:self.count]
