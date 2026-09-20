class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        
        odd = head
        even = head.next
        even_head = even  # Keep reference to start of even list
        
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            
            even.next = odd.next
            even = even.next
            
        # Connect the end of the odd list to the start of the even list
        odd.next = even_head
        
        return head