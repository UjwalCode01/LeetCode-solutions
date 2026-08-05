class Solution(object):

  def findDisappearedNumbers(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    # First pass: Mark numbers as visited by making the value at index (val - 1) negative
    for num in nums:
      idx = abs(num) - 1
      if nums[idx] > 0:
        nums[idx] = -nums[idx]

    # Second pass: Collect all 1-based indices that were not visited (stayed positive)
    res = []
    for i in range(len(nums)):
      if nums[i] > 0:
        res.append(i + 1)

    return res