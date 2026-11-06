# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def numComponents(self, head: ListNode | None, nums: list[int]) -> int:
        num_set = set(nums)
        components = 0
        in_component = False
        
        curr = head
        while curr:
            if curr.val in num_set:
                # If we are not currently inside a component, start a new one
                if not in_component:
                    components += 1
                    in_component = True
            else:
                # We hit a node not in nums, so the current component ends
                in_component = False
                
            curr = curr.next
            
        return components