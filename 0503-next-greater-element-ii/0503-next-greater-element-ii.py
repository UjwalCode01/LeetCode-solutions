class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = []  # Stores indices
        
        # Traverse twice to handle circular array behavior
        for i in range(2 * n):
            curr_idx = i % n
            while stack and nums[stack[-1]] < nums[curr_idx]:
                prev_idx = stack.pop()
                res[prev_idx] = nums[curr_idx]
            if i < n:
                stack.append(curr_idx)
                
        return res