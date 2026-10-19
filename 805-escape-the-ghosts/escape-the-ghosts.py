class Solution:
    def escapeGhosts(self, ghosts: list[list[int]], target: list[int]) -> bool:
        # Calculate your minimum steps (Manhattan distance from origin to target)
        my_distance = abs(target[0]) + abs(target[1])
        
        # Check against every ghost's minimum steps to the target
        for ghost in ghosts:
            ghost_distance = abs(ghost[0] - target[0]) + abs(ghost[1] - target[1])
            # If any ghost can reach the target in fewer or equal steps, you cannot escape
            if ghost_distance <= my_distance:
                return False
                
        return True