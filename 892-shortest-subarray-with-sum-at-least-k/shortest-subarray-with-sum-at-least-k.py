from collections import deque

class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:
        n = len(nums)
        # Prefix sum array to compute subarray sums in O(1) time
        prefix_sums = [0] * (n + 1)
        for i in range(n):
            prefix_sums[i + 1] = prefix_sums[i] + nums[i]
            
        ans = n + 1  # Initialize with a value larger than possible length
        mono_q = deque()  # Monotonic queue to store indices of prefix sums
        
        for y in range(n + 1):
            # For the current prefix sum at index y, check if there are any valid 
            # previous starting indices x such that prefix_sums[y] - prefix_sums[x] >= k
            while mono_q and prefix_sums[y] - prefix_sums[mono_q[0]] >= k:
                ans = min(ans, y - mono_q.popleft())
                
            # Maintain monotonicity: remove indices from the back of the queue 
            # where the prefix sum is greater than or equal to the current prefix sum at y
            while mono_q and prefix_sums[y] <= prefix_sums[mono_q[-1]]:
                mono_q.pop()
                
            mono_q.append(y)
            
        return ans if ans <= n else -1