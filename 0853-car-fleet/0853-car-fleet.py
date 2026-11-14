class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # Pair position and speed, then sort closest to target first
        cars = sorted(zip(position, speed), reverse=True)
        
        fleets = 0
        last_time = 0.0  # Arrival time of the fleet currently ahead
        
        for pos, spd in cars:
            time = (target - pos) / spd
            
            # If this car takes longer than the fleet ahead, it can't catch up
            # and starts a new fleet. Otherwise, it merges into the fleet ahead.
            if time > last_time:
                fleets += 1
                last_time = time
                
        return fleets