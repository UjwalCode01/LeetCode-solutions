class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # Handle the edge case where one of the numbers is "0"
        if num1 == "0" or num2 == "0":
            return "0"
        
        # The maximum possible length of the product result is len(num1) + len(num2)
        res = [0] * (len(num1) + len(num2))
        
        # Reverse loop through both strings to multiply digit by digit from right to left
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                # Convert character digits to actual integers
                digit1 = ord(num1[i]) - ord('0')
                digit2 = ord(num2[j]) - ord('0')
                
                # Multiply the digits and add to the current position in the result array
                mul = digit1 * digit2
                p1, p2 = i + j, i + j + 1
                total_sum = mul + res[p2]
                
                # Update positions with carry and remainder
                res[p2] = total_sum % 10
                res[p1] += total_sum // 10
                
        # Convert the array of integers back to a string, skipping leading zeros
        result_str = []
        for digit in res:
            if not (len(result_str) == 0 and digit == 0):
                result_str.append(str(digit))
                
        return "".join(result_str)