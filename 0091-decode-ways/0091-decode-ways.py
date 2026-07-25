class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == '0':
            return 0
        
        # prev2 represents dp[i-2], prev1 represents dp[i-1]
        prev2 = 1  # Base case for empty string
        prev1 = 1  # Base case for string of length 1 (since s[0] != '0')
        
        for i in range(1, len(s)):
            current = 0
            
            # 1. Single digit check: valid if s[i] is between '1' and '9'
            if s[i] != '0':
                current += prev1
                
            # 2. Two digit check: valid if '10' <= s[i-1:i+1] <= '26'
            two_digit = int(s[i-1:i+1])
            if 10 <= two_digit <= 26:
                current += prev2
                
            # Update pointers for the next iteration
            prev2 = prev1
            prev1 = current
            
        return prev1