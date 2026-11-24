class Solution(object):
    def sumSubseqWidths(self, nums):
        mod = 10**9 + 7
        nums.sort()
        n = len(nums)
        ans = 0
        pow2 = 1

        for i in range(n):
            ans = (ans + nums[i] * pow2) % mod
            pow2 = (pow2 * 2) % mod

        pow2 = 1
        for i in range(n - 1, -1, -1):
            ans = (ans - nums[i] * pow2) % mod
            pow2 = (pow2 * 2) % mod

        return ans