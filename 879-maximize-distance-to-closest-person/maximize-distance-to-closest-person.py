class Solution:
    def maxDistToClosest(self, seats: list[int]) -> int:
        n = len(seats)
        max_dist = 0
        prev_person = -1
        
        for i in range(n):
            if seats[i] == 1:
                if prev_person == -1:
                    # Case 1: Leading zeros (distance from start to the first person)
                    max_dist = max(max_dist, i)
                else:
                    # Case 2: Zeros between two people
                    max_dist = max(max_dist, (i - prev_person) // 2)
                prev_person = i
                
        # Case 3: Trailing zeros (distance from the last person to the end)
        max_dist = max(max_dist, n - 1 - prev_person)
        
        return max_dist