class Solution(object):
    def diffWaysToCompute(self, expression):
        res = []
        
        for i, char in enumerate(expression):
            if char in "+-*":
                # Split expression into left and right sub-problems
                left_results = self.diffWaysToCompute(expression[:i])
                right_results = self.diffWaysToCompute(expression[i+1:])
                
                # Combine results from left and right sub-problems
                for l in left_results:
                    for r in right_results:
                        if char == '+':
                            res.append(l + r)
                        elif char == '-':
                            res.append(l - r)
                        elif char == '*':
                            res.append(l * r)
        
        # Base case: purely numeric string
        if not res:
            res.append(int(expression))
            
        return res