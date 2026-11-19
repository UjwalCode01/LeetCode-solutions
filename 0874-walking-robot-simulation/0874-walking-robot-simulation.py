class Solution:
    def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        # Directions in clockwise order: North, East, South, West
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir_idx = 0  # Starts facing North
        
        x, y = 0, 0
        max_dist_sq = 0
        
        # Store obstacles in a set of tuples for O(1) lookup
        obstacle_set = {(ox, oy) for ox, oy in obstacles}
        
        for cmd in commands:
            if cmd == -2:
                # Turn left 90 degrees (counter-clockwise)
                dir_idx = (dir_idx - 1) % 4
            elif cmd == -1:
                # Turn right 90 degrees (clockwise)
                dir_idx = (dir_idx + 1) % 4
            else:
                # Move forward `cmd` units, one step at a time
                dx, dy = directions[dir_idx]
                for _ in range(cmd):
                    next_x, next_y = x + dx, y + dy
                    if (next_x, next_y) in obstacle_set:
                        # Stop before the obstacle and move to the next command
                        break
                    x, y = next_x, next_y
                    max_dist_sq = max(max_dist_sq, x * x + y * y)
                    
        return max_dist_sq