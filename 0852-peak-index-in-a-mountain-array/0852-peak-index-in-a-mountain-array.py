class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        left = 0
        right = len(arr) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # If the middle element is less than the next element, 
            # we are on the rising slope, so the peak is to the right.
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            # Otherwise, we are on the falling slope or at the peak, 
            # so the peak is at mid or to the left.
            else:
                right = mid
                
        # When left equals right, we have found the peak index.
        return left