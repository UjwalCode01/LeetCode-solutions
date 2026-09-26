class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        result = []
        
        # Traverse both strings from right to left
        while i >= 0 or j >= 0 or carry:
            digit1 = ord(num1[i]) - ord('0') if i >= 0 else 0
            digit2 = ord(num2[j]) - ord('0') if j >= 0 else 0
            
            total = digit1 + digit2 + carry
            carry = total // 10
            result.append(str(total % 10))
            
            i -= 1
            j -= 1
            
        return "".join(result[::-1])