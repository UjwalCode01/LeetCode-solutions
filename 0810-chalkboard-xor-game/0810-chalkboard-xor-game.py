class Solution:
    def xorGame(self, nums: list[int]) -> bool:
        xor_sum = 0
        for num in nums:
            xor_sum ^= num
            
        # Agar initial XOR sum 0 hai, ya fir array ki length even hai, toh Alice jeet jayegi
        return xor_sum == 0 or len(nums) % 2 == 0