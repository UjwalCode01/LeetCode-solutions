class Solution(object):
    def predictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        memo = {}
        
        def helper(i, j):
            # Base case: only one number left
            if i == j:
                return nums[i]
            if (i, j) in memo:
                return memo[(i, j)]
            
            # Choose the optimal score difference by picking either the left or right end
            pick_left = nums[i] - helper(i + 1, j)
            pick_right = nums[j] - helper(i, j - 1)
            
            memo[(i, j)] = max(pick_left, pick_right)
            return memo[(i, j)]
            
        return helper(0, len(nums) - 1) >= 0