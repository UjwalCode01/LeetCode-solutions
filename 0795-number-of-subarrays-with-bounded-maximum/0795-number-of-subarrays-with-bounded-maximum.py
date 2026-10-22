class Solution:
    def numSubarrayBoundedMax(self, nums: list[int], left: int, right: int) -> int:
        def count(bound: int) -> int:
            res = 0
            current = 0
            for x in nums:
                if x <= bound:
                    current += 1
                    res += current
                else:
                    current = 0
            return res
        
        return count(right) - count(left - 1)