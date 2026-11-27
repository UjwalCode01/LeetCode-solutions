class Solution(object):
    def numPermsDISequence(self, s):
        MOD = 10**9 + 7
        n = len(s)
        dp = [1]

        for i in range(1, n + 1):
            pref = [0] * (i + 1)
            for k in range(i):
                pref[k + 1] = (pref[k] + dp[k]) % MOD

            new_dp = [0] * (i + 1)
            if s[i - 1] == "I":
                for j in range(i + 1):
                    new_dp[j] = pref[min(j, i)]
            else:
                for j in range(i):
                    new_dp[j] = (pref[i] - pref[j]) % MOD

            dp = new_dp

        return sum(dp) % MOD