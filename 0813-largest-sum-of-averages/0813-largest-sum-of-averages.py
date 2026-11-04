class Solution:
    def largestSumOfAverages(self, nums: list[int], k: int) -> float:
        memo = {}
        
        def search(i: int, k: int) -> float:
            if (i, k) in memo:
                return memo[(i, k)]
            if k == 1:
                return sum(nums[i:]) / (len(nums) - i)
            
            res = 0
            curr_sum = 0
            for j in range(i, len(nums) - k + 1):
                curr_sum += nums[j]
                avg = curr_sum / (j - i + 1)
                res = max(res, avg + search(j + 1, k - 1))
                
            memo[(i, k)] = res
            return res

        return search(0, k)