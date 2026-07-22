class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        len1, len2, len3 = len(s1), len(s2), len(s3)

        # Base sanity check: combined length must match s3
        if len1 + len2 != len3:
            return False

        # dp[i][j] will be True if s1[:i] and s2[:j] form s3[:i+j]
        dp = [[False] * (len2 + 1) for _ in range(len1 + 1)]

        # Empty s1 and empty s2 form empty s3
        dp[0][0] = True

        # Fill the first column (only using s1)
        for i in range(1, len1 + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]

        # Fill the first row (only using s2)
        for j in range(1, len2 + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]

        # Fill the rest of the DP table
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                # Match s1's character
                from_s1 = dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]
                # Match s2's character
                from_s2 = dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]

                dp[i][j] = from_s1 or from_s2

        return dp[len1][len2]