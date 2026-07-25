# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        if not head or left == right:
            return head
        
        # Step 1: Create a dummy node to simplify edge cases (e.g., left = 1)
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # Step 2: Advance `prev` to the node right before position `left`
        for _ in range(left - 1):
            prev = prev.next
            
        # `curr` will be the first node of the sublist to reverse
        curr = prev.next
        
        # Step 3: Reverse the nodes between `left` and `right` in-place
        for _ in range(right - left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp
            
        return dummy.next