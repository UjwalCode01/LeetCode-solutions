class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Create a dummy node that points to the head of the list
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        
        # Ensure there are at least two nodes left to swap
        while current.next and current.next.next:
            # Identify the two nodes to be swapped
            first = current.next
            second = current.next.next
            
            # Perform the swap by changing pointers
            first.next = second.next
            second.next = first
            current.next = second
            
            # Move the pointer two nodes ahead for the next pair
            current = first
            
        return dummy.next