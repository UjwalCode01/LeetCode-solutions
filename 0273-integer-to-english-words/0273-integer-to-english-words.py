class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"

        # Lookup tables
        LESS_THAN_20 = [
            "", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
            "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", 
            "Sixteen", "Seventeen", "Eighteen", "Nineteen"
        ]
        
        TENS = [
            "", "", "Twenty", "Thirty", "Forty", "Fifty", 
            "Sixty", "Seventy", "Eighty", "Ninety"
        ]
        
        THOUSANDS = ["", "Thousand", "Million", "Billion"]

        def helper(n):
            """Converts a number < 1000 to English words."""
            if n == 0:
                return ""
            elif n < 20:
                return LESS_THAN_20[n] + " "
            elif n < 100:
                return TENS[n // 10] + " " + helper(n % 10)
            else:
                return LESS_THAN_20[n // 100] + " Hundred " + helper(n % 100)

        result = ""
        i = 0

        # Process digits in groups of 3
        while num > 0:
            if num % 1000 != 0:
                result = helper(num % 1000) + THOUSANDS[i] + " " + result
            num //= 1000
            i += 1

        return result.strip()