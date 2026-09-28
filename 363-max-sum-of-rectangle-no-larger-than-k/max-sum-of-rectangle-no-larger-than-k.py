import bisect

class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        
        # Ensure n <= m to minimize column pairs
        if n > m:
            matrix = [list(row) for row in zip(*matrix)]
            m, n = n, m
            
        max_sum = float('-inf')
        
        for left in range(n):
            row_sums = [0] * m
            for right in range(left, n):
                for r in range(m):
                    row_sums[r] += matrix[r][right]
                
                # Binary Search on Prefix Sums for 1D array
                prefix_sums = [0]
                curr_sum = 0
                for s in row_sums:
                    curr_sum += s
                    target = curr_sum - k
                    idx = bisect.bisect_left(prefix_sums, target)
                    if idx < len(prefix_sums):
                        max_sum = max(max_sum, curr_sum - prefix_sums[idx])
                        if max_sum == k:
                            return k  # Best possible answer found
                    
                    bisect.insort(prefix_sums, curr_sum)
                    
        return max_sum