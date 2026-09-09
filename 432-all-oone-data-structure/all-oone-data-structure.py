class Node:
    def __init__(self, count):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None

class AllOne:

    def __init__(self):
        self.map = {}
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node_after(self, new_node, prev_node):
        new_node.prev = prev_node
        new_node.next = prev_node.next
        prev_node.next.prev = new_node
        prev_node.next = new_node

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def inc(self, key):
        if key in self.map:
            curr_node = self.map[key]
            next_count = curr_node.count + 1
            curr_node.keys.remove(key)
            
            if curr_node.next != self.tail and curr_node.next.count == next_count:
                next_node = curr_node.next
            else:
                next_node = Node(next_count)
                self._add_node_after(next_node, curr_node)
            
            next_node.keys.add(key)
            self.map[key] = next_node
            
            if not curr_node.keys:
                self._remove_node(curr_node)
        else:
            if self.head.next != self.tail and self.head.next.count == 1:
                first_node = self.head.next
            else:
                first_node = Node(1)
                self._add_node_after(first_node, self.head)
            
            first_node.keys.add(key)
            self.map[key] = first_node

    def dec(self, key):
        curr_node = self.map[key]
        curr_node.keys.remove(key)
        
        if curr_node.count == 1:
            del self.map[key]
        else:
            prev_count = curr_node.count - 1
            if curr_node.prev != self.head and curr_node.prev.count == prev_count:
                prev_node = curr_node.prev
            else:
                prev_node = Node(prev_count)
                self._add_node_after(prev_node, curr_node.prev)
            
            prev_node.keys.add(key)
            self.map[key] = prev_node

        if not curr_node.keys:
            self._remove_node(curr_node)

    def getMaxKey(self):
        if self.tail.prev == self.head:
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self):
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))