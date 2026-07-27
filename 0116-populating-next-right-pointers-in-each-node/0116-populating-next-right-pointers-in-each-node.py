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
        
        # Start with the root node
        leftmost = root
        
        # Traverse level by level until we reach the leaf level
        while leftmost.left:
            curr = leftmost
            
            # Iterate through the nodes on the current level
            while curr:
                # Connection 1: Connect left child to right child of the same parent
                curr.left.next = curr.right
                
                # Connection 2: Connect right child to the left child of the next parent
                if curr.next:
                    curr.right.next = curr.next.left
                
                # Move to the next node across the same level
                curr = curr.next
            
            # Move down to the first node of the next level
            leftmost = leftmost.left
            
        return root