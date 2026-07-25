class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()  # Step 1: Sort to bring duplicates together
        
        def backtrack(start, current_subset):
            # Append a copy of the current subset to results
            res.append(list(current_subset))
            
            for i in range(start, len(nums)):
                # Step 2: Skip duplicate elements at the same depth
                if i > start and nums[i] == nums[i - 1]:
                    continue
                
                # Include element
                current_subset.append(nums[i])
                # Recurse for next elements
                backtrack(i + 1, current_subset)
                # Backtrack
                current_subset.pop()
                
        backtrack(0, [])
        return res