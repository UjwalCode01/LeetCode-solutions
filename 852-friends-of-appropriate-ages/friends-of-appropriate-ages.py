class Solution:
    def numFriendRequests(self, ages: list[int]) -> int:
        # Count the frequency of each age
        age_count = [0] * 121
        for age in ages:
            age_count[age] += 1
            
        total_requests = 0
        
        # Check all pairs of ages from 1 to 120
        for age_x in range(1, 121):
            count_x = age_count[age_x]
            if count_x == 0:
                continue
                
            for age_y in range(1, 121):
                count_y = age_count[age_y]
                if count_y == 0:
                    continue
                
                # Apply the restriction rules where x will NOT send a request to y:
                # 1. age[y] <= 0.5 * age[x] + 7
                # 2. age[y] > age[x]
                # 3. age[y] > 100 and age[x] < 100 (covered by age[y] > age[x])
                if age_y <= 0.5 * age_x + 7:
                    continue
                if age_y > age_x:
                    continue
                if age_y > 100 and age_x < 100:
                    continue
                
                # If valid, add requests
                total_requests += count_x * count_y
                
                # If x and y are the same age, a person cannot send a request to themselves,
                # so we subtract the count of people of that age.
                if age_x == age_y:
                    total_requests -= count_x
                    
        return total_requests