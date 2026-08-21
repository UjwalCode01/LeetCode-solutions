class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        next_greater = {}
        stack = []

        # Process nums2 to build the mapping of next greater elements
        for num in nums2:
            # While stack is not empty and current element is greater than top of stack
            while stack and num > stack[-1]:
                next_greater[stack.pop()] = num
            stack.append(num)

        # Elements remaining in stack have no next greater element
        while stack:
            next_greater[stack.pop()] = -1

        # Map each element in nums1 to its precomputed result
        return [next_greater[num] for num in nums1]