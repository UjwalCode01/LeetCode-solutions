class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def count_zeroes(x: int) -> int:
            res = 0
            while x > 0:
                res += x // 5
                x //= 5
            return res

        # Binary search for the smallest x such that count_zeroes(x) >= k
        left, right = 0, 5 * k + 1
        ans = right
        
        while left <= right:
            mid = (left + right) // 2
            if count_zeroes(mid) >= k:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
                
        # If the exact count k is found, there are 5 numbers (x through x+4)
        return 5 if count_zeroes(ans) == k else 0