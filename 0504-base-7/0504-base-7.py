class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"

        is_negative = num < 0
        num = abs(num)
        digits = []

        while num > 0:
            digits.append(str(num % 7))
            num //= 7

        if is_negative:
            digits.append("-")

        return "".join(reversed(digits))