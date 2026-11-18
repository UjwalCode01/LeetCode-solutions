class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: list[list[int]]) -> int:
        import heapq
        
        # Max heap to store fuel capacities of stations we've passed
        max_heap = []
        
        # Append target as a virtual station with 0 fuel to handle the final stretch
        stations.append([target, 0])
        
        current_fuel = startFuel
        prev_position = 0
        stops = 0
        
        for position, fuel in stations:
            # Distance we need to travel to reach the current station/target
            current_fuel -= (position - prev_position)
            
            # If we don't have enough fuel to reach this station, refuel from the best past station
            while current_fuel < 0 and max_heap:
                current_fuel += -heapq.heappop(max_heap)
                stops += 1
                
            # If we still don't have enough fuel, it's impossible to reach
            if current_fuel < 0:
                return -1
                
            # Push this station's fuel into the max-heap for future use
            heapq.heappush(max_heap, -fuel)
            prev_position = position
            
        return stops