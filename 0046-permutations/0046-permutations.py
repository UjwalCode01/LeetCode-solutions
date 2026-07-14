class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        
        def backtrack(first):
            # If all integers are used up
            if first == len(nums):
                result.append(list(nums))
                return
            
            for i in range(first, len(nums)):
                # Place i-th integer first in the current permutation
                nums[first], nums[i] = nums[i], nums[first]
                
                # Use next integers to complete the permutations
                backtrack(first + 1)
                
                # Backtrack: restore the original array state
                nums[first], nums[i] = nums[i], nums[first]
                
        backtrack(0)
        return result