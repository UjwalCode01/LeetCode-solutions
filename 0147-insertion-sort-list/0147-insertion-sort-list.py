# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        curr = head

        while curr:
            # Save the next node to process
            next_node = curr.next

            # Find position to insert curr in the sorted portion
            prev = dummy
            while prev.next and prev.next.val < curr.val:
                prev = prev.next

            # Insert curr between prev and prev.next
            curr.next = prev.next
            prev.next = curr

            # Move to the next unsorted node
            curr = next_node

        return dummy.next