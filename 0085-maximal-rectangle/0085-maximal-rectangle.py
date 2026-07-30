class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        
        rows = len(matrix)
        cols = len(matrix[0])
        heights = [0] * cols
        max_area = 0

        # Helper function: Largest Rectangle in Histogram (LeetCode 84)
        def largestRectangleArea(heights):
            stack = []
            max_h_area = 0
            # Append 0 height to flush out all remaining bars in stack
            for i, h in enumerate(heights + [0]):
                while stack and heights[stack[-1]] >= h:
                    height = heights[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    max_h_area = max(max_h_area, height * width)
                stack.append(i)
            return max_h_area

        # Process each row as the base of the histogram
        for row in matrix:
            for c in range(cols):
                if row[c] == '1':
                    heights[c] += 1
                else:
                    heights[c] = 0
            
            # Find max rectangle for the current histogram state
            max_area = max(max_area, largestRectangleArea(heights))

        return max_area