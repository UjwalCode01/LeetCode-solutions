class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:
            return "0"
            
        result = []
        
        # Determine the sign
        if (numerator < 0) ^ (denominator < 0):
            result.append("-")
            
        # Work with positive numbers
        num = abs(numerator)
        den = abs(denominator)
        
        # Integer part
        result.append(str(num // den))
        remainder = num % den
        
        if remainder == 0:
            return "".join(result)
            
        # Fractional part
        result.append(".")
        remainder_map = {}
        
        while remainder != 0:
            # If remainder has been seen before, a cycle is detected
            if remainder in remainder_map:
                idx = remainder_map[remainder]
                result.insert(idx, "(")
                result.append(")")
                break
                
            # Store index where this remainder's quotient digit will be placed
            remainder_map[remainder] = len(result)
            
            remainder *= 10
            result.append(str(remainder // den))
            remainder %= den
            
        return "".join(result)