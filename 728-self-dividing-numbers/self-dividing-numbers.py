class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        result = []
        for num in range(left, right + 1):
            s_num = str(num)
            # Check if '0' is in the number and if it's divisible by each digit
            if '0' not in s_num and all(num % int(digit) == 0 for digit in s_num):
                result.append(num)
        return result