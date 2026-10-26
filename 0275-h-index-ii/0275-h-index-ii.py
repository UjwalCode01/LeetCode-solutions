class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left, right = 0, n - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # If the citation count is greater than or equal to the number of papers remaining
            if citations[mid] >= n - mid:
                right = mid - 1  # Try to find a larger h-index on the left
            else:
                left = mid + 1   # Need a higher citation count, move right
                
        # left points to the first valid h-index position
        return n - left