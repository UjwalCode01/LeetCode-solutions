class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.queue = [0] * k
        self.capacity = k
        self.head = 0
        self.count = 0  # Number of elements currently in queue

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        
        # Calculate insert index (rear)
        tail = (self.head + self.count) % self.capacity
        self.queue[tail] = value
        self.count += 1
        return True

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        
        # Move head to next position
        self.head = (self.head + 1) % self.capacity
        self.count -= 1
        return True

    def Front(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        # Tail index is (head + count - 1) % capacity
        tail = (self.head + self.count - 1) % self.capacity
        return self.queue[tail]

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.count == 0

    def isFull(self):
        """
        :rtype: bool
        """
        return self.count == self.capacity