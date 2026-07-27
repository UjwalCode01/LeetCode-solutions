"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        if not root:
            return None
        
        curr = root
        
        # Traverse level by level
        while curr:
            # Dummy node acts as the head/start of the next level's linked list
            dummy = Node(0)
            tail = dummy
            
            # Traverse across the current level using 'next' pointers
            while curr:
                if curr.left:
                    tail.next = curr.left
                    tail = tail.next
                
                if curr.right:
                    tail.next = curr.right
                    tail = tail.next
                
                curr = curr.next
            
            # Move curr to the first node of the next level
            curr = dummy.next
            
        return root