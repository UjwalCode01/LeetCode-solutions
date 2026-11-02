class Solution:
    def bestRotation(self, nums: list[int]) -> int:
        n = len(nums)
        # change[k] track karega ki k rotation par score kitna change hota hai
        change = [0] * n
        
        for i, num in enumerate(nums):
            # Element nums[i] rotation step (i - num + 1 + n) % n par point lose karta hai
            change[(i - num + 1 + n) % n] -= 1
            
        max_score = -1
        best_k = 0
        curr_score = 0
        
        # k = 0 par initial score calculation (optional step shortcut using change array)
        # Hum score changes track karke best k nikalte hain
        for k in range(n):
            # Rotate karne par index 0 wala element end mein chala jata hai, jisse 1 point add hota hai
            curr_score += change[k] + 1
            if curr_score > max_score:
                max_score = curr_score
                best_k = k
                
        return best_k