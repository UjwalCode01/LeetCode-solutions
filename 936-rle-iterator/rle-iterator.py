class RLEIterator(object):

    def __init__(self, encoding):
        self.encoding = encoding
        self.index = 0

    def next(self, n):
        while self.index < len(self.encoding) and n > self.encoding[self.index]:
            n -= self.encoding[self.index]
            self.index += 2

        if self.index >= len(self.encoding):
            return -1

        self.encoding[self.index] -= n
        return self.encoding[self.index + 1]