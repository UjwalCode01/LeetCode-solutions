class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if not ops:
            return m * n
        
        # Find the minimum rows and minimum columns affected across all operations
        min_row = min(op[0] for op in ops)
        min_col = min(op[1] for op in ops)
        
        return min_row * min_col