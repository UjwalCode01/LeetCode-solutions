class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        
        # Step 1: Monotonic stack build karna
        for digit in num:
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        
        # Step 2: Agar abhi bhi k > 0 hai (e.g., num = "12345"), toh last digits hatao
        if k > 0:
            stack = stack[:-k]
        
        # Step 3: Leading zeroes ko hatana aur empty stack handling
        result = "".join(stack).lstrip('0')
        
        return result if result else "0"