class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()  # Sort to handle duplicates easily
        used = [False] * len(nums)
        
        def backtrack(current_path):
            if len(current_path) == len(nums):
                result.append(list(current_path))
                return
            
            for i in range(len(nums)):
                # Skip if already used in this path
                if used[i]:
                    continue
                
                # Skip duplicates: if the current number is same as previous, 
                # and the previous one was NOT used in the current recursion branch
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                
                # Make choice
                used[i] = True
                current_path.append(nums[i])
                
                # Explore
                backtrack(current_path)
                
                # Undo choice
                current_path.pop()
                used[i] = False
                
        backtrack([])
        return result