class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m, n = len(mat), len(mat[0])
        
        # If reshaping isn't possible or legal, return original matrix
        if m * n != r * c:
            return mat
        
        # Initialize result matrix filled with 0s
        reshaped = [[0] * c for _ in range(r)]
        
        # Map 1D index to original and new 2D indices
        for i in range(m * n):
            reshaped[i // c][i % c] = mat[i // n][i % n]
            
        return reshaped