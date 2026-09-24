class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_length = 0
        
        for i in range(len(nums)):
            # If the node is not visited yet
            if nums[i] != -1:
                start = i
                count = 0
                
                # Traverse the cycle
                while nums[start] != -1:
                    temp = nums[start]
                    nums[start] = -1  # Mark as visited
                    start = temp
                    count += 1
                
                max_length = max(max_length, count)
                
        return max_length