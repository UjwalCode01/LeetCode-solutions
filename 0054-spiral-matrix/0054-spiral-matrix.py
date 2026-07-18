class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        
        result = []
        
        # Initialize boundaries
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        
        while top <= bottom and left <= right:
            # 1. Traverse from Left to Right along the top boundary
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1  # Move the top boundary down
            
            # 2. Traverse from Top to Bottom along the right boundary
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1  # Move the right boundary left
            
            # Check if boundaries have crossed before moving left/up
            if top <= bottom:
                # 3. Traverse from Right to Left along the bottom boundary
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1  # Move the bottom boundary up
                
            if left <= right:
                # 4. Traverse from Bottom to Top along the left boundary
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1  # Move the left boundary right
                
        return result