class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []

        def backtrack(start, current_combination):
            # Base case: if combination length reaches k
            if len(current_combination) == k:
                res.append(list(current_combination))
                return

            # Optimization: only loop up to the point where there are enough numbers remaining to complete length k
            needed = k - len(current_combination)
            for i in range(start, n - needed + 2):
                current_combination.append(i)
                backtrack(i + 1, current_combination)
                current_combination.pop()  # Backtrack

        backtrack(1, [])
        return res