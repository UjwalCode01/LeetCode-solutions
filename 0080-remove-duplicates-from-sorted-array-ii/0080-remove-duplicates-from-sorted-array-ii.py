class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)
        
        # 'k' pointer batata hai ki agla valid element kahan place hoga
        k = 2
        
        for i in range(2, len(nums)):
            # Agar current element nums[i], k-2 wale element se alag hai,
            # toh iska matlab is element ki count 2 se zyada nahi hui hai.
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1
                
        return k