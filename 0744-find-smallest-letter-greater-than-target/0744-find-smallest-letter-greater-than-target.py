class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        left, right = 0, len(letters) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
                
        # If left reaches len(letters), it wraps around to 0
        return letters[left % len(letters)]