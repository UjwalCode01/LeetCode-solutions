class Solution:
    def numFactoredBinaryTrees(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        arr.sort()
        
        # dp[x] stores the number of binary trees with root x
        dp = {x: 1 for x in arr}
        
        for i in range(len(arr)):
            x = arr[i]
            for j in range(i):
                left = arr[j]
                if x % left == 0:
                    right = x // left
                    if right in dp:
                        dp[x] = (dp[x] + dp[left] * dp[right]) % MOD
                        
        return sum(dp.values()) % MOD