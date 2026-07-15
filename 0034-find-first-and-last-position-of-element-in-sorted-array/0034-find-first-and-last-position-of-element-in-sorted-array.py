class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def binary_search(find_first):
            left, right = 0, len(nums) - 1
            bound_idx = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    # Found target; record index
                    bound_idx = mid
                    if find_first:
                        # Keep looking left for the starting boundary
                        right = mid - 1
                    else:
                        # Keep looking right for the ending boundary
                        left = mid + 1
            return bound_idx

        # Find first and last occurrences
        first = binary_search(find_first=True)
        # If the first position is -1, the element doesn't exist at all
        if first == -1:
            return [-1, -1]
            
        last = binary_search(find_first=False)
        return [first, last]