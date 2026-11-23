class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        sum_a = sum(aliceSizes)
        sum_b = sum(bobSizes)
        diff = (sum_b - sum_a) // 2
        bob_set = set(bobSizes)

        for x in aliceSizes:
            y = x + diff
            if y in bob_set:
                return [x, y]