class Solution(object):

  def findDuplicates(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    res = []

    for num in nums:
      val = abs(num)
      idx = val - 1

      # If the element at index (val - 1) is negative, we've seen val before
      if nums[idx] < 0:
        res.append(val)
      else:
        # Mark as visited by making it negative
        nums[idx] = -nums[idx]

    return res