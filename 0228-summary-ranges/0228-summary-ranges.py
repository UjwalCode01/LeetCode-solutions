class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        result = []
        i = 0
        n = len(nums)
        
        while i < n:
            start = nums[i]
            
            # Move i forward as long as numbers are consecutive
            while i + 1 < n and nums[i + 1] == nums[i] + 1:
                i += 1
                
            end = nums[i]
            
            # Format the range string
            if start == end:
                result.append(str(start))
            else:
                result.append("{}->{}".format(start, end))
                
            i += 1
            
        return result