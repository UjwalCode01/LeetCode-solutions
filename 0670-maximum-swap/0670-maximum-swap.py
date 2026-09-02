class Solution(object):
    def maximumSwap(self, num):
        """:type num: int
        :rtype: int
        """
        digits = list(str(num))
        # Record the last occurrence of each digit (0-9)
        last = {int(val): i for i, val in enumerate(digits)}
        
        for i, val in enumerate(digits):
            # Check if there is a strictly larger digit available later in the number
            for d in range(9, int(val), -1):
                if last.get(d, -1) > i:
                    # Swap and return the new number
                    j = last[d]
                    digits[i], digits[j] = digits[j], digits[i]
                    return int("".join(digits))
                    
        return num