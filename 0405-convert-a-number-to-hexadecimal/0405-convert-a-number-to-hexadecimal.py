class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
        
        # Mapping for hexadecimal characters
        hex_map = "0123456789abcdef"
        
        # Convert to 32-bit unsigned integer (handles negative numbers)
        num &= 0xFFFFFFFF
        
        result = []
        
        while num > 0:
            # Extract last 4 bits
            digit = num & 15
            result.append(hex_map[digit])
            # Right shift by 4 bits
            num >>= 4
            
        # Reverse because digits were extracted from right to left
        return "".join(reversed(result))