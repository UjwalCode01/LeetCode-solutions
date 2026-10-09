class Solution:
    def judgePoint24(self, cards: list[int]) -> bool:
        def solve(nums):
            if len(nums) == 1:
                # Floating point precision check
                return abs(nums[0] - 24) < 1e-6

            # Har possible pair (i, j) choose karenge
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i != j:
                        # Baaki ke remaining numbers collect karo
                        next_nums = [nums[k] for k in range(len(nums)) if k != i and k != j]

                        a, b = nums[i], nums[j]
                        
                        # Possible results generation
                        candidates = [a + b, a - b, a * b]
                        if abs(b) > 1e-6:  # Avoid division by zero
                            candidates.append(a / b)

                        # Recursive call for each candidate result
                        for res in candidates:
                            if solve(next_nums + [res]):
                                return True

            return False

        return solve(cards)