class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0   # Minimum open brackets balance
        high = 0  # Maximum open brackets balance
        
        for char in s:
            if char == '(':
                low += 1
                high += 1
            elif char == ')':
                low -= 1
                high -= 1
            elif char == '*':
                low -= 1   # '*' can be ')'
                high += 1  # '*' can be '('
            
            # Agar high < 0 ho gaya, matlab invalid ')' zyada ho gaye
            if high < 0:
                return False
            
            # low kabhi negative nahi ho sakta (empty string ke case me 0 reset)
            if low < 0:
                low = 0
                
        # Agar low == 0 hai, toh sahi balance ban sakta hai
        return low == 0