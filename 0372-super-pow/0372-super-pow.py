class Solution(object):

    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        MOD = 1337
        a %= MOD
        result = 1

        for digit in b:
            # Raise current result to power 10 and multiply by a^digit
            result = (pow(result, 10, MOD) * pow(a, digit, MOD)) % MOD

        return result