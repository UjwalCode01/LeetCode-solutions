class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0
            
        jumps = 0
        current_jump_end = 0
        farthest = 0
        
        for i in range(len(nums) - 1):
            # Update the farthest index we can reach from the current position
            farthest = max(farthest, i + nums[i])
            
            # If we've reached the end of the range for the current jump
            if i == current_jump_end:
                jumps += 1
                current_jump_end = farthest
                
                # If the farthest we can reach already covers the last index, we can stop
                if current_jump_end >= len(nums) - 1:
                    break
                    
        return jumps