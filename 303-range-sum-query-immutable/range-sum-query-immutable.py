class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.prefix_sums = []
        current_sum = 0
        for num in nums:
            current_sum += num
            self.prefix_sums.append(current_sum)

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        if left == 0:
            return self.prefix_sums[right]
        return self.prefix_sums[right] - self.prefix_sums[left - 1]