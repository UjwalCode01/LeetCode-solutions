class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = [] # Will store tuples of (index, height)
        max_area = 0
        
        for i, h in enumerate(heights):
            start = i
            # If the current height is smaller than the height at the top of the stack,
            # we must pop from the stack and calculate the areas.
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                # Width is the current index minus the index where that height started
                width = i - idx
                max_area = max(max_area, height * width)
                # The current bar can extend backwards to the index of the popped bar
                start = idx
                
            # Push the current height and its adjusted starting index onto the stack
            stack.append((start, h))
            
        # Clear out any remaining bars left in the stack
        for idx, height in stack:
            width = len(heights) - idx
            max_area = max(max_area, height * width)
            
        return max_area