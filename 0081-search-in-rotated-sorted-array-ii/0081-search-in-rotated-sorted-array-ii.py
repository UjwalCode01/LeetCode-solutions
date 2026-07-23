class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return True
            
            # Duplicates Handle karne ke liye: jab left, mid aur right teeno same ho
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
            # Check karo ki Left Half sorted hai kya
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # Target left half me hai
                else:
                    left = mid + 1   # Target right half me hai
            # Agar Left Sorted nahi hai, matlab Right Half Sorted hai
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1   # Target right half me hai
                else:
                    right = mid - 1  # Target left half me hai
                    
        return False