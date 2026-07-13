class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :type rtype: int
        """
        # Constants for 32-bit signed integer limits
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Handle overflow edge case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine the sign of the result
        negative = (dividend < 0) ^ (divisor < 0)

        # Work with absolute values
        a = abs(dividend)
        b = abs(divisor)
        quotient = 0

        # Exponentially subtract the divisor using bit shifts
        while a >= b:
            temp = b
            multiple = 1
            # Keep shifting left (doubling) as long as it fits inside 'a'
            while a >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            
            a -= temp
            quotient += multiple

        # Apply the sign and clamp the final result to 32-bit limits
        result = -quotient if negative else quotient
        return max(INT_MIN, min(INT_MAX, result))