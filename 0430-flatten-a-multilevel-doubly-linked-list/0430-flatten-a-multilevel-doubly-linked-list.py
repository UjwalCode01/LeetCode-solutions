class Solution(object):
    def flatten(self, head):
        if not head:
            return None
        
        # Pointer to keep track of the previously processed node
        dummy = Node(0, None, head, None)
        prev = dummy
        
        stack = [head]
        
        while stack:
            curr = stack.pop()
            
            # Connect prev and curr
            prev.next = curr
            curr.prev = prev
            
            # If curr has a next node, push it to stack first
            # (so it gets processed after the child branch)
            if curr.next:
                stack.append(curr.next)
                
            # If curr has a child, push it to stack second
            # (so it gets popped and processed immediately next)
            if curr.child:
                stack.append(curr.child)
                curr.child = None  # Clear the child pointer as required
                
            prev = curr
            
        # Detach the dummy head from the actual head
        head.prev = None
        return head