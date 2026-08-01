# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def isPalindrome(self, head):
        """:type head: Optional[ListNode]
        :rtype: bool
        """
        if not head or not head.next:
            return True

        # 1. Find the middle of the linked list (Fast & Slow pointers)
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Reverse the second half of the list
        prev = None
        curr = slow
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp

        # 3. Compare the first half and reversed second half
        first_half = head
        second_half = prev  # prev is the head of the reversed half
        while second_half:
            if first_half.val != second_half.val:
                return False
            first_half = first_half.next
            second_half = second_half.next

        return True
        