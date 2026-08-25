class Solution(object):

  def findUnsortedSubarray(self, nums):
    """:type nums: List[int]

    :rtype: int
    """
    n = len(nums)
    max_seen = float('-inf')
    min_seen = float('inf')

    right = -1
    left = -1

    # Find the right boundary of the unsorted subarray
    for i in range(n):
      if nums[i] < max_seen:
        right = i
      else:
        max_seen = nums[i]

    # Find the left boundary of the unsorted subarray
    for i in range(n - 1, -1, -1):
      if nums[i] > min_seen:
        left = i
      else:
        min_seen = nums[i]

    # If already sorted, return 0
    if right == -1:
      return 0

    return right - left + 1