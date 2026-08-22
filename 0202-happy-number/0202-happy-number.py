class Solution(object):

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            # Calculate the sum of the squares of its digits
            n = sum(int(digit) ** 2 for digit in str(n))

        return n == 1