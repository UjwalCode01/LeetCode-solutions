from collections import defaultdict

class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        if not mat or not mat[0]:
            return []

        rows, cols = len(mat), len(mat[0])
        diagonals = defaultdict(list)

        # Step 1: Group matrix elements by index sum (r + c)
        for r in range(rows):
            for c in range(cols):
                diagonals[r + c].append(mat[r][c])

        result = []

        # Step 2: Build the result array
        for d in range(rows + cols - 1):
            if d % 2 == 0:
                # Upward direction: reverse the natural iteration order
                result.extend(diagonals[d][::-1])
            else:
                # Downward direction: keep standard top-to-bottom order
                result.extend(diagonals[d])

        return result