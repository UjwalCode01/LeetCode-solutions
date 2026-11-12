class Solution:
    def splitIntoFibonacci(self, num: str) -> list[int]:
        n = len(num)
        
        def backtrack(index, path):
            # If we reached the end of the string and have at least 3 numbers, it's a valid Fibonacci sequence
            if index == n and len(path) >= 3:
                return path
            
            for i in range(index, n):
                # Leading zero check: if the number starts with '0' and its length > 1, it's invalid
                if num[index] == '0' and i > index:
                    break
                
                curr_str = num[index:i+1]
                curr_num = int(curr_str)
                
                # Check 32-bit signed integer constraint
                if curr_num >= 2**31:
                    break
                
                # If we have at least 2 numbers, the next number must equal their sum
                if len(path) >= 2:
                    if curr_num > path[-1] + path[-2]:
                        break # Since numbers are growing, larger slices will also exceed
                    elif curr_num < path[-1] + path[-2]:
                        continue
                
                # Recurse with the current number added to path
                result = backtrack(i + 1, path + [curr_num])
                if result:
                    return result
                    
            return []

        return backtrack(0, [])