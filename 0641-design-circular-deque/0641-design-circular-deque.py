class MyCircularDeque:

    def __init__(self, k: int):
        """[cite: 2]"""
        self.k = k
        self.queue = [0] * k
        self.head = 0
        self.tail = 0
        self.size = 0

    def insertFront(self, value: int) -> bool:
        """[cite: 2]"""
        if self.isFull():
            return False
        # Move head backwards circularly
        self.head = (self.head - 1 + self.k) % self.k
        self.queue[self.head] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        """[cite: 2]"""
        if self.isFull():
            return False
        self.queue[self.tail] = value
        # Move tail forward circularly
        self.tail = (self.tail + 1) % self.k
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        """[cite: 2]"""
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.k
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        """[cite: 2]"""
        if self.isEmpty():
            return False
        self.tail = (self.tail - 1 + self.k) % self.k
        self.size -= 1
        return True

    def getFront(self) -> int:
        """[cite: 2]"""
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def getRear(self) -> int:
        """[cite: 2]"""
        if self.isEmpty():
            return -1
        return self.queue[(self.tail - 1 + self.k) % self.k]

    def isEmpty(self) -> bool:
        """[cite: 2]"""
        return self.size == 0

    def isFull(self) -> bool:
        """[cite: 2]"""
        return self.size == self.k