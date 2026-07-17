import heapq

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        # Create a dummy node to easily construct the result linked list
        dummy = ListNode(0)
        curr = dummy
        
        # Initialize the heap
        min_heap = []
        
        # Push the head of each non-empty linked list into the heap
        # We include 'i' (the index) as a tie-breaker so Python doesn't 
        # try to compare the ListNode objects directly if values are equal.
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(min_heap, (l.val, i, l))
                
        # Process the heap until it's empty
        while min_heap:
            val, i, node = heapq.heappop(min_heap)
            
            # Connect the smallest node to our merged list
            curr.next = node
            curr = curr.next
            
            # If the popped node has a next node, push it into the heap
            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))
                
        return dummy.next