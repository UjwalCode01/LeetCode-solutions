class Solution:
    def reversePairs(self, nums: list[int]) -> int:
        def merge_sort(start: int, end: int) -> int:
            if start >= end:
                return 0
            
            mid = (start + end) // 2
            count = merge_sort(start, mid) + merge_sort(mid + 1, end)
            
            # Count reverse pairs between left half [start..mid] and right half [mid+1..end]
            j = mid + 1
            for i in range(start, mid + 1):
                while j <= end and nums[i] > 2 * nums[j]:
                    j += 1
                count += j - (mid + 1)
            
            # Standard merge step
            nums[start:end + 1] = sorted(nums[start:end + 1])
            return count

        return merge_sort(0, len(nums) - 1)