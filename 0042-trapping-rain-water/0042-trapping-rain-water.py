class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water_trapped = 0
        
        while left < right:
            # The water level is limited by the smaller boundary
            if left_max < right_max:
                left += 1
                # Update the maximum height from the left
                left_max = max(left_max, height[left])
                # Add the trapped water above the current bar
                water_trapped += left_max - height[left]
            else:
                right -= 1
                # Update the maximum height from the right
                right_max = max(right_max, height[right])
                # Add the trapped water above the current bar
                water_trapped += right_max - height[right]
                
        return water_trapped