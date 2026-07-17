# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or k == 1:
            return head
        
        # Dummy node to handle head changes easily
        dummy = ListNode(0)
        dummy.next = head
        
        # 'group_prev' tracks the node right before the current k-group
        group_prev = dummy
        
        while True:
            # Check if there are at least k nodes left to reverse
            kth = self.getKthNode(group_prev, k)
            if not kth:
                break
                
            # Track the node right after this k-group
            group_next = kth.next
            
            # Reverse the current group
            prev, curr = kth.next, group_prev.next
            while curr != group_next:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
                
            # Re-link the reversed group back into the main list
            temp = group_prev.next  # This was the old head, now it's the tail of the reversed group
            group_prev.next = kth   # Point the previous group to the new head (kth node)
            group_prev = temp       # Move group_prev to the tail for the next iteration
            
        return dummy.next

    def getKthNode(self, curr, k):
        """Helper to find the k-th node from the current position."""
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr