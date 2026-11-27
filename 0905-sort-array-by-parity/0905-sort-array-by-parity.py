class Solution(object):
    def sortArrayByParity(self, nums):
        even_idx = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i], nums[even_idx] = nums[even_idx], nums[i]
                even_idx += 1
        return nums