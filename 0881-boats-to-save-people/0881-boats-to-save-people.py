class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()
        
        left = 0
        right = len(people) - 1
        boats = 0
        
        while left <= right:
            # Agar sabse halke aur sabse bhaari dono ek boat mein aa sakte hain
            if people[left] + people[right] <= limit:
                left += 1
            
            # Sabse bhaari person har step mein boat le raha hai
            right -= 1
            boats += 1
            
        return boats