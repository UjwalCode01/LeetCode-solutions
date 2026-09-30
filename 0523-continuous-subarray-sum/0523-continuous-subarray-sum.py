class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # Map to store {remainder: earliest_index}
        # Initialize with remainder 0 at index -1 to handle subarrays starting from index 0
        remainder_map = {0: -1}
        running_sum = 0
        
        for i, num in enumerate(nums):
            running_sum += num
            remainder = running_sum % k
            
            # If remainder was seen before, check if subarray length >= 2
            if remainder in remainder_map:
                if i - remainder_map[remainder] >= 2:
                    return True
            else:
                # Store the first occurrence of this remainder
                remainder_map[remainder] = i
                
        return False