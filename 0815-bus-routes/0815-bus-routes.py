from collections import defaultdict, deque
from typing import List

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        # Map each bus stop to the list of bus indices that visit it
        stop_to_buses = defaultdict(list)
        for bus_idx, route in enumerate(routes):
            for stop in route:
                stop_to_buses[stop].append(bus_idx)
        
        # Queue stores tuples of (current_bus_idx, bus_count)
        queue = deque()
        visited_buses = set()
        visited_stops = set()
        
        # Initialize queue with all buses that pass through the source
        for bus_idx in stop_to_buses[source]:
            queue.append((bus_idx, 1))
            visited_buses.add(bus_idx)
            
        visited_stops.add(source)
        
        while queue:
            bus_idx, count = queue.popleft()
            
            # Check all stops on the current bus route
            for stop in routes[bus_idx]:
                if stop == target:
                    return count
                
                # If we haven't visited this stop yet, explore other buses passing through it
                if stop not in visited_stops:
                    visited_stops.add(stop)
                    for next_bus_idx in stop_to_buses[stop]:
                        if next_bus_idx not in visited_buses:
                            visited_buses.add(next_bus_idx)
                            queue.append((next_bus_idx, count + 1))
                            
        return -1