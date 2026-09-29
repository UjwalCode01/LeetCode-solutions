class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        left, right = 0, len(nums) - 1
        moves = 0
        
        while left < right:
            moves += nums[right] - nums[left]
            left += 1
            right -= 1
            
        return moves