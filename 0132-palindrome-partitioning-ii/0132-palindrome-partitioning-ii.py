class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n <= 1:
            return 0

        # cuts[i] stores min cuts for prefix s[0...i]
        cuts = [i for i in range(n)]

        def expand(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                if left == 0:
                    cuts[right] = 0
                else:
                    cuts[right] = min(cuts[right], cuts[left - 1] + 1)
                left -= 1
                right += 1

        for i in range(n):
            expand(i, i)       # Odd length palindromes
            expand(i, i + 1)   # Even length palindromes

        return cuts[-1]