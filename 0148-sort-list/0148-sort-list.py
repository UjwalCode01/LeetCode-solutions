# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Base case: empty list or single node
        if not head or not head.next:
            return head

        # Step 1: Split the list into two halves using fast & slow pointers
        left = head
        right = self._get_mid(head)
        tmp = right.next
        right.next = None
        right = tmp

        # Step 2: Recursively sort both halves
        left = self.sortList(left)
        right = self.sortList(right)

        # Step 3: Merge the two sorted halves
        return self._merge(left, right)

    def _get_mid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def _merge(self, list1, list2):
        dummy = ListNode(0)
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        if list2:
            tail.next = list2

        return dummy.next