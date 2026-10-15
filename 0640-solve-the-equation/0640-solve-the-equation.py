class Solution:
    def solveEquation(self, equation: str) -> str:
        def parse(expr):
            # Helper to parse a side of the equation
            # We pad with '+' if it starts with a number/variable for uniform splitting
            if expr[0] not in "+-":
                expr = "+" + expr
            
            coeff = 0
            const = 0
            i = 0
            n = len(expr)
            
            while i < n:
                sign = 1 if expr[i] == '+' else -1
                i += 1
                
                # Extract number or x
                j = i
                while j < n and expr[j] not in "+-":
                    j += 1
                
                token = expr[i:j]
                if 'x' in token:
                    # Handle cases like "+x", "-x", "+2x", "-10x"
                    num_str = token.replace('x', '')
                    if num_str == '':
                        coeff += sign * 1
                    else:
                        coeff += sign * int(num_str)
                else:
                    const += sign * int(token)
                
                i = j
                
            return coeff, const

        left_str, right_str = equation.split('=')
        l_coeff, l_const = parse(left_str)
        r_coeff, r_const = parse(right_str)
        
        # Bring x terms to left, constants to right
        # (l_coeff - r_coeff) * x = r_const - l_const
        diff_coeff = l_coeff - r_coeff
        diff_const = r_const - l_const
        
        if diff_coeff == 0:
            if diff_const == 0:
                return "Infinite solutions"
            else:
                return "No solution"
        
        ans = diff_const // diff_coeff
        return f"x={ans}"