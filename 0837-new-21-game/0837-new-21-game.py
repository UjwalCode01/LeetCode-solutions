class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        # If Alice stops immediately (k == 0) or n is large enough to cover all possible scores up to k - 1 + maxPts
        if k == 0 or n >= k + maxPts:
            return 1.0
        
        # dp[i] represents the probability of getting point i
        dp = [0.0] * (n + 1)
        dp[0] = 1.0
        
        window_sum = 1.0 # Sum of probabilities in the sliding window of size maxPts
        ans = 0.0
        
        for i in range(1, n + 1):
            dp[i] = window_sum / maxPts
            
            # If i < k, Alice can still draw, so add dp[i] to the window sum
            if i < k:
                window_sum += dp[i]
            else:
                # If i >= k, Alice stops drawing, so this is a valid terminal state contributing to the answer
                ans += dp[i]
                
            # If the window size exceeds maxPts, remove the element falling out of the window from the left
            if i - maxPts >= 0:
                if i - maxPts < k:
                    window_sum -= dp[i - maxPts]
                    
        return ans
        