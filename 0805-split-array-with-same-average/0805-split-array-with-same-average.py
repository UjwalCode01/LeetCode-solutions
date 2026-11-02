class Solution:
    def splitArraySameAverage(self, nums: list[int]) -> bool:
        n = len(nums)
        if n < 2:
            return False
        
        total_sum = sum(nums)
        
        # Check mathematically if any valid subset size k exists
        # total_sum * k must be divisible by n
        possible_sizes = []
        for k in range(1, n // 2 + 1):
            if (total_sum * k) % n == 0:
                possible_sizes.append(k)
                
        if not possible_sizes:
            return False
        
        # Meet in the middle optimization
        half = n // 2
        left_sums = [set() for _ in range(half + 1)]
        left_sums[0].add(0)
        
        for num in nums[:half]:
            for k in range(half - 1, -1, -1):
                for s in left_sums[k]:
                    left_sums[k + 1].add(s + num)
                    
        right_sums = [set() for _ in range(n - half + 1)]
        right_sums[0].add(0)
        
        for num in nums[half:]:
            for k in range(n - half - 1, -1, -1):
                for s in right_sums[k]:
                    right_sums[k + 1].add(s + num)
                    
        for k in possible_sizes:
            for left_k in range(max(0, k - (n - half)), min(half, k) + 1):
                right_k = k - left_k
                target_sum = (total_sum * k) // n
                
                for s in left_sums[left_k]:
                    if (target_sum - s) in right_sums[right_k]:
                        return True
                        
        return False