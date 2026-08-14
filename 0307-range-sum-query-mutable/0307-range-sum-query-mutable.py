class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.n = len(nums)
        self.nums = nums[:]  # Keep track of original values to compute differences during updates
        self.tree = [0] * (self.n + 1)
        
        # Build the Fenwick Tree
        for i in range(self.n):
            self._add(i + 1, nums[i])

    def _add(self, index, delta):
        """Helper to add delta to tree at 1-based index."""
        while index <= self.n:
            self.tree[index] += delta
            index += index & (-index)

    def _prefix_sum(self, index):
        """Helper to query sum from index 1 to index (1-based)."""
        s = 0
        while index > 0:
            s += self.tree[index]
            index -= index & (-index)
        return s

    def update(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        # Calculate difference between new value and current value
        delta = val - self.nums[index]
        self.nums[index] = val
        self._add(index + 1, delta)

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        # sum(left..right) = prefix_sum(right) - prefix_sum(left - 1)
        return self._prefix_sum(right + 1) - self._prefix_sum(left)