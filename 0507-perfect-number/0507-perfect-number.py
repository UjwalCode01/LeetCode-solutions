class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False

        # 1 is always a proper divisor
        total_sum = 1
        
        # Check divisors up to sqrt(num)
        i = 2
        while i * i <= num:
            if num % i == 0:
                total_sum += i
                # Add the corresponding paired divisor if it's distinct
                if i * i != num:
                    total_sum += num // i
            i += 1

        return total_sum == num