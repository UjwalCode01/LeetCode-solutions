class Node:
    def __init__(self, val=0):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        # Optimize traversal from head or tail depending on index position
        if index < self.size // 2:
            curr = self.head.next
            for _ in range(index):
                curr = curr.next
        else:
            curr = self.tail.prev
            for _ in range(self.size - 1 - index):
                curr = curr.prev
        return curr.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index < 0:
            index = 0
            
        # Find the predecessor of the new node
        pred = self.head
        for _ in range(index):
            pred = pred.next
        succ = pred.next
        
        # Insert new node between pred and succ
        new_node = Node(val)
        new_node.prev = pred
        new_node.next = succ
        pred.next = new_node
        succ.prev = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        
        # Find the node to delete
        curr = self.head.next
        for _ in range(index):
            curr = curr.next
            
        # Unlink curr from the list
        pred = curr.prev
        succ = curr.next
        pred.next = succ
        succ.prev = pred
        self.size -= 1