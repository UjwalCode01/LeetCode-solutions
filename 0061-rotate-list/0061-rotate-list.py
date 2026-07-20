# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        # Base cases handle karte hain
        if not head or not head.next or k == 0:
            return head
        
        # 1. Length nikalte hain aur tail node dhoodte hain
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
            
        # 2. Agar k length se bada hai toh modulo le lenge
        k = k % length
        if k == 0:
            return head # Agar effective rotation 0 hai, toh mehnat bachi
            
        # 3. Last node ko head se jod kar circular loop banayein
        tail.next = head
        
        # 4. Naye tail tak travel karein (length - k steps from start)
        steps_to_new_tail = length - k
        new_tail = head
        for _ in range(steps_to_new_tail - 1):
            new_tail = new_tail.next
            
        # 5. Naya head set karein aur loop ko break karein
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head