class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        counts = {}
        duplicate = -1
        missing = -1
        
        # Count occurrences of each number
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            
        # Identify duplicate and missing numbers in the range 1 to n
        for i in range(1, n + 1):
            if counts.get(i, 0) == 2:
                duplicate = i
            elif counts.get(i, 0) == 0:
                missing = i
                
        return [duplicate, missing]
        