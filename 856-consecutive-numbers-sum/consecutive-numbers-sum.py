class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        count = 0
        k = 1
        
        # Loop while the sum of first (k - 1) integers is less than n
        while k * (k - 1) // 2 < n:
            rem = n - (k * (k - 1) // 2)
            if rem % k == 0:
                count += 1
            k += 1
            
        return count