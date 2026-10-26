class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        
        def backtrack(index: int, path: str, eval_val: int, prev_operand: int):
            # Base Case: if we've processed all digits
            if index == len(num):
                if eval_val == target:
                    res.append(path)
                return
            
            for i in range(index, len(num)):
                # Skip numbers with leading zeros (e.g., "05" is invalid, but "0" is valid)
                if i > index and num[index] == '0':
                    break
                
                str_val = num[index:i + 1]
                curr_val = int(str_val)
                
                # If it's the first number, no operator is needed yet
                if index == 0:
                    backtrack(i + 1, str_val, curr_val, curr_val)
                else:
                    # Addition
                    backtrack(i + 1, path + "+" + str_val, eval_val + curr_val, curr_val)
                    # Subtraction
                    backtrack(i + 1, path + "-" + str_val, eval_val - curr_val, -curr_val)
                    # Multiplication (adjust for precedence by undoing prev_operand)
                    backtrack(i + 1, path + "*" + str_val, eval_val - prev_operand + prev_operand * curr_val, prev_operand * curr_val)
                    
        backtrack(0, "", 0, 0)
        return res