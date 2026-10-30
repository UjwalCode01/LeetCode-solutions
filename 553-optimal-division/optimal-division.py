class Solution:
    def optimalDivision(self, nums: list[int]) -> str:
        if len(nums) == 1:
            return str(nums[0])
        if len(nums) == 2:
            return f"{nums[0]}/{nums[1]}"
        
        # Put parentheses around everything after the first element
        denominator = "/".join(map(str, nums[1:]))
        return f"{nums[0]}/({denominator})"