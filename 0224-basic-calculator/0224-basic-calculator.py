class Solution(object):
    def calculate(self, s):
        stack = []
        curr_number = 0
        current_result = 0
        sign = 1  # 1 for '+', -1 for '-'

        for char in s:
            if char.isdigit():
                curr_number = curr_number * 10 + int(char)
            elif char in '+-':
                current_result += sign * curr_number
                curr_number = 0
                sign = 1 if char == '+' else -1
            elif char == '(':
                # Push the running result and current sign onto stack
                stack.append(current_result)
                stack.append(sign)
                # Reset for the inner sub-expression
                current_result = 0
                sign = 1
            elif char == ')':
                # Complete evaluation for the inside of parentheses
                current_result += sign * curr_number
                curr_number = 0
                # Apply the sign before the opening '('
                current_result *= stack.pop()
                # Add the result before the opening '('
                current_result += stack.pop()

        return current_result + (sign * curr_number)