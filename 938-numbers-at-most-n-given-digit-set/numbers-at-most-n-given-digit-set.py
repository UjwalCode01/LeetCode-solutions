class Solution(object):

    def atMostNGivenDigitSet(self, digits, n):
        s = str(n)
        m = len(s)
        k = len(digits)
        total = 0

        for i in range(1, m):
            total += k ** i

        for i in range(m):
            has_same = False
            for d in digits:
                if d < s[i]:
                    total += k ** (m - i - 1)
                elif d == s[i]:
                    has_same = True
            if not has_same:
                return total

        return total + 1