class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        curr = 1
        k -= 1  # We start at prefix 1, so decrement 1 step
        
        while k > 0:
            steps = self._count_steps(n, curr, curr + 1)
            
            if steps <= k:
                # Target is NOT in this subtree; jump to the next sibling
                k -= steps
                curr += 1
            else:
                # Target IS in this subtree; go down to the first child
                curr *= 10
                k -= 1
                
        return curr

    def _count_steps(self, n: int, prefix1: int, prefix2: int) -> int:
        """Count how many numbers exist in the prefix tree rooted at prefix1."""
        steps = 0
        while prefix1 <= n:
            steps += min(n + 1, prefix2) - prefix1
            prefix1 *= 10
            prefix2 *= 10
        return steps