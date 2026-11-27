class Solution(object):
    def superpalindromesInRange(self, left, right):
        l = int(left)
        r = int(right)
        limit = int(r**0.5) + 1
        ans = 0

        for half in range(1, 100000):
            s_half = str(half)

            even_k = int(s_half + s_half[::-1])
            if even_k <= limit:
                sq = even_k * even_k
                if l <= sq <= r and str(sq) == str(sq)[::-1]:
                    ans += 1

            odd_k = int(s_half + s_half[:-1][::-1])
            if odd_k <= limit:
                sq = odd_k * odd_k
                if l <= sq <= r and str(sq) == str(sq)[::-1]:
                    ans += 1

        return ans