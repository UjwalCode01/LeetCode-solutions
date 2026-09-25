class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        low = matrix[0][0]
        high = matrix[n - 1][n - 1]

        def countLessEqual(mid):
            count = 0
            row, col = n - 1, 0  # Start from bottom-left
            while row >= 0 and col < n:
                if matrix[row][col] <= mid:
                    count += row + 1  # Add all elements in this column up to `row`
                    col += 1
                else:
                    row -= 1
            return count

        while low < high:
            mid = (low + high) // 2
            if countLessEqual(mid) < k:
                low = mid + 1
            else:
                high = mid

        return low