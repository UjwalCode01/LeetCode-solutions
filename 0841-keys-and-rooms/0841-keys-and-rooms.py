class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        visited = set()
        stack = [0]
        
        while stack:
            room = stack.pop()
            if room not in visited:
                visited.add(room)
                # Add all keys found in the current room to the stack
                for key in rooms[room]:
                    if key not in visited:
                        stack.append(key)
                        
        return len(visited) == len(rooms)