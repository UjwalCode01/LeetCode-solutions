import random

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):

    def __init__(self, head):
        """
        :type head: Optional[ListNode]
        """
        self.head = head

    def getRandom(self):
        """
        :rtype: int
        """
        chosen_val = None
        curr = self.head
        i = 1
        
        while curr:
            # Pick the current element with probability 1/i
            if random.randint(1, i) == 1:
                chosen_val = curr.val
            curr = curr.next
            i += 1
            
        return chosen_val