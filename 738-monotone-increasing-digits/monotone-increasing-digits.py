class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        digits = list(str(n))
        length = len(digits)
        marker = length
        
        # Right to Left check karein
        for i in range(length - 1, 0, -1):
            if digits[i - 1] > digits[i]:
                digits[i - 1] = str(int(digits[i - 1]) - 1)
                marker = i
                
        # Marker ke baad ke sare digits ko 9 bana dein
        for i in range(marker, length):
            digits[i] = '9'
            
        return int("".join(digits))