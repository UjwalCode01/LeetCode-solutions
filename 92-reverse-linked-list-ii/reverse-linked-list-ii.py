# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if not head or left == right:
            return head

        # Dummy node simplifies edge cases (e.g., when left = 1)
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Step 1: Reach the node just before the 'left' position
        for _ in range(left - 1):
            prev = prev.next

        # Step 2: Reverse the sublist from 'left' to 'right'
        curr = prev.next
        for _ in range(right - left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next