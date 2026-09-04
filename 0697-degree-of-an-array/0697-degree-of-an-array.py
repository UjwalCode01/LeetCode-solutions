class Solution(object):
    def findShortestSubArray(self, nums):
        """:type nums: List[int] :rtype: int"""
        left, right, count = {}, {}, {}
        
        for i, x in enumerate(nums):
            if x not in left:
                left[x] = i
            right[x] = i
            count[x] = count.get(x, 0) + 1
            
        degree = max(count.values())
        min_length = len(nums)
        
        for x in count:
            if count[x] == degree:
                min_length = min(min_length, right[x] - left[x] + 1)
                
        return min_length