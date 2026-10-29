class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        n = len(arr)
        # Suffix minimum array banate hain
        right_min = [0] * (n + 1)
        right_min[n] = float('inf')
        
        for i in range(n - 1, -1, -1):
            right_min[i] = min(right_min[i + 1], arr[i])
            
        chunks = 0
        left_max = float('-inf')
        
        for i in range(n):
            left_max = max(left_max, arr[i])
            # Agar left ka maximum chhota ya barabar hai right ke minimum se, toh chunk ban sakta hai
            if left_max <= right_min[i + 1]:
                chunks += 1
                
        return chunks