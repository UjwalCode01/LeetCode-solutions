"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None

        # Step 1: Create interleaved cloned nodes (A -> A' -> B -> B')
        curr = head
        while curr:
            new_node = Node(curr.val, curr.next)
            curr.next = new_node
            curr = new_node.next

        # Step 2: Assign random pointers for cloned nodes
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # Step 3: Separate the original list and the cloned list
        curr = head
        copied_head = head.next
        while curr:
            copied_node = curr.next
            curr.next = copied_node.next
            if copied_node.next:
                copied_node.next = copied_node.next.next
            curr = curr.next

        return copied_head