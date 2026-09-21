class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        if n == 0:
            return 1
        
        # Base case for 1-digit numbers (0 through 9)
        ans = 10
        unique_choices = 9
        available_digits = 9
        
        # Calculate unique numbers for length 2 up to n
        for i in range(2, n + 1):
            unique_choices *= available_digits
            ans += unique_choices
            available_digits -= 1
            
        return ans