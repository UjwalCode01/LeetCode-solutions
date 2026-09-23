class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        stack = []
        third = float('-inf')  # Represents nums[k]

        # Iterate from right to left
        for num in reversed(nums):
            # If current element is smaller than third (nums[k]), 
            # we found a valid nums[i] < nums[k] < nums[j]
            if num < third:
                return True
            
            # Maintain monotonic stack (decreasing order)
            while stack and stack[-1] < num:
                third = stack.pop()
            
            stack.append(num)
            
        return False