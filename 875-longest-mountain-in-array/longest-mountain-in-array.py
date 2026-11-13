class Solution:
    def longestMountain(self, arr: list[int]) -> int:
        n = len(arr)
        max_len = 0
        i = 1
        
        while i < n - 1:
            # Check if arr[i] is a peak
            if arr[i - 1] < arr[i] > arr[i + 1]:
                left = i
                right = i
                
                # Expand left to find the start of the mountain
                while left > 0 and arr[left - 1] < arr[left]:
                    left -= 1
                    
                # Expand right to find the end of the mountain
                while right < n - 1 and arr[right] > arr[right + 1]:
                    right += 1
                    
                # Calculate current mountain length and update max_len
                current_len = right - left + 1
                max_len = max(max_len, current_len)
                
                # Jump 'i' to the end of the current mountain to optimize
                i = right
            else:
                i += 1
                
        return max_len