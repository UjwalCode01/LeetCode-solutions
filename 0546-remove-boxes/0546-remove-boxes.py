class Solution:
    def removeBoxes(self, boxes: list[int]) -> int:
        memo = {}

        def dp(l, r, k):
            if l > r:
                return 0
            
            # Optimization: Merge consecutive boxes of the same color on the left
            while l < r and boxes[l] == boxes[l + 1]:
                l += 1
                k += 1

            state = (l, r, k)
            if state in memo:
                return memo[state]

            # Option 1: Remove the current group of boxes [l...l] along with its 'k' extras
            res = (k + 1) * (k + 1) + dp(l + 1, r, 0)

            # Option 2: Try to merge boxes[l] with another identical box further right
            for i in range(l + 1, r + 1):
                if boxes[i] == boxes[l]:
                    res = max(res, dp(l + 1, i - 1, 0) + dp(i, r, k + 1))

            memo[state] = res
            return res

        return dp(0, len(boxes) - 1, 0)